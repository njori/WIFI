$BASE_URL = "http://localhost:5000"
$API_URL = "$BASE_URL/api"

Write-Host "====== WiFi API Test Suite ======" -ForegroundColor Cyan

# Test 1: Health Check
Write-Host "`nTest 1: Health Check" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "$BASE_URL/" -UseBasicParsing -ErrorAction Stop
    Write-Host "✓ Root endpoint: $($response.StatusCode)" -ForegroundColor Green
    $json = $response.Content | ConvertFrom-Json
    Write-Host "  Application: $($json.application)"
    Write-Host "  Version: $($json.version)"
} catch {
    Write-Host "✗ Failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 2: API Health
Write-Host "`nTest 2: API Health" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "$API_URL/health" -UseBasicParsing -ErrorAction Stop
    Write-Host "✓ Health: $($response.StatusCode)" -ForegroundColor Green
    $json = $response.Content | ConvertFrom-Json
    Write-Host "  Database: $($json.database)"
    Write-Host "  Server: $($json.server)"
} catch {
    Write-Host "✗ Failed: $($_.Exception.Message)" -ForegroundColor Red
}

# Test 3: Register
Write-Host "`nTest 3: User Registration" -ForegroundColor Yellow
$registerBody = @{
    email = "testuser@example.com"
    password = "TestPass123!"
    first_name = "Test"
    last_name = "User"
} | ConvertTo-Json

try {
    $response = Invoke-WebRequest -Uri "$API_URL/auth/register" `
        -Method POST `
        -ContentType "application/json" `
        -Body $registerBody `
        -UseBasicParsing -ErrorAction Stop
    Write-Host "✓ Registration: $($response.StatusCode)" -ForegroundColor Green
    $json = $response.Content | ConvertFrom-Json
    Write-Host "  Message: $($json.message)"
} catch {
    if ($_.Exception.Response.StatusCode.Value -eq 400) {
        Write-Host "⚠ User likely already exists" -ForegroundColor Yellow
    } else {
        Write-Host "✗ Failed: $($_.Exception.Response.StatusCode.Value)" -ForegroundColor Red
    }
}

# Test 4: Login
Write-Host "`nTest 4: User Login" -ForegroundColor Yellow
$loginBody = @{
    email = "testuser@example.com"
    password = "TestPass123!"
} | ConvertTo-Json

try {
    $response = Invoke-WebRequest -Uri "$API_URL/auth/login" `
        -Method POST `
        -ContentType "application/json" `
        -Body $loginBody `
        -UseBasicParsing -ErrorAction Stop
    Write-Host "✓ Login: $($response.StatusCode)" -ForegroundColor Green
    $json = $response.Content | ConvertFrom-Json
    $script:authToken = $json.data.access_token
    Write-Host "  Token obtained: $($script:authToken.Substring(0, 20))..." -ForegroundColor Cyan
} catch {
    Write-Host "✗ Failed: $($_.Exception.Response.StatusCode.Value)" -ForegroundColor Red
}

# Test 5: Get Current User
Write-Host "`nTest 5: Get Current User (Authenticated)" -ForegroundColor Yellow
if ($script:authToken) {
    try {
        $headers = @{ "Authorization" = "Bearer $script:authToken" }
        $response = Invoke-WebRequest -Uri "$API_URL/auth/me" `
            -Headers $headers `
            -UseBasicParsing -ErrorAction Stop
        Write-Host "✓ Get User: $($response.StatusCode)" -ForegroundColor Green
        $json = $response.Content | ConvertFrom-Json
        Write-Host "  Email: $($json.data.email)"
        Write-Host "  Name: $($json.data.first_name) $($json.data.last_name)"
    } catch {
        Write-Host "✗ Failed: $($_.Exception.Response.StatusCode.Value)" -ForegroundColor Red
    }
}

# Test 6: Dashboard
Write-Host "`nTest 6: Dashboard Overview (Authenticated)" -ForegroundColor Yellow
if ($script:authToken) {
    try {
        $headers = @{ "Authorization" = "Bearer $script:authToken" }
        $response = Invoke-WebRequest -Uri "$API_URL/dashboard/overview" `
            -Headers $headers `
            -UseBasicParsing -ErrorAction Stop
        Write-Host "✓ Dashboard: $($response.StatusCode)" -ForegroundColor Green
        $json = $response.Content | ConvertFrom-Json
        Write-Host "  Total Routers: $($json.data.summary.total_routers)"
        Write-Host "  Total Networks: $($json.data.summary.total_networks)"
        Write-Host "  Total Devices: $($json.data.summary.total_devices)"
    } catch {
        Write-Host "✗ Failed: $($_.Exception.Response.StatusCode.Value)" -ForegroundColor Red
    }
}

Write-Host "`n====== Test Complete ======`n" -ForegroundColor Cyan
