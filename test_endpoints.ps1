$BASE_URL = "http://localhost:5000/api"

Write-Host "`n═══════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "WiFi Management System - API Endpoint Test" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════`n" -ForegroundColor Cyan

# Step 1: Login to get auth token
Write-Host "Step 1: Authenticating..." -ForegroundColor Yellow
$loginBody = @{
    email = "admin@example.com"
    password = "Admin@123"
} | ConvertTo-Json

try {
    $loginResponse = Invoke-WebRequest -Uri "$BASE_URL/auth/login" `
        -Method POST `
        -ContentType "application/json" `
        -Body $loginBody `
        -UseBasicParsing -ErrorAction Stop
    
    $loginData = $loginResponse.Content | ConvertFrom-Json
    $token = $loginData.data.access_token
    $headers = @{ "Authorization" = "Bearer $token" }
    
    Write-Host "✓ Authenticated successfully" -ForegroundColor Green
    Write-Host "  Token: $($token.Substring(0, 30))...`n" -ForegroundColor Cyan
} catch {
    Write-Host "✗ Login failed" -ForegroundColor Red
    exit
}

# Function to test endpoint
function Test-Endpoint {
    param(
        [string]$Endpoint,
        [string]$Description,
        [string]$Method = "GET"
    )
    
    try {
        $response = Invoke-WebRequest -Uri "$BASE_URL$Endpoint" `
            -Headers $headers `
            -Method $Method `
            -UseBasicParsing -ErrorAction Stop
        
        $data = $response.Content | ConvertFrom-Json
        Write-Host "✓ $Description" -ForegroundColor Green
        Write-Host "  Endpoint: $Endpoint" -ForegroundColor Gray
        Write-Host "  Status: $($response.StatusCode)" -ForegroundColor Gray
        
        if ($null -ne $data.data) {
            if ($data.data -is [array]) {
                Write-Host "  Items: $($data.data.Count)" -ForegroundColor Cyan
            }
        }
        Write-Host ""
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.Value
        if ($statusCode -eq 404) {
            Write-Host "✗ $Description - NOT FOUND" -ForegroundColor Yellow
        } else {
            Write-Host "✗ $Description - ERROR $statusCode" -ForegroundColor Red
        }
        Write-Host "  Endpoint: $Endpoint" -ForegroundColor Gray
        Write-Host ""
    }
}

# Test Authentication Endpoints
Write-Host "AUTHENTICATION ENDPOINTS" -ForegroundColor Magenta
Write-Host "───────────────────────" -ForegroundColor Magenta
Test-Endpoint "/auth/me" "Get Current User"
Test-Endpoint "/auth/refresh" "Refresh Token" "POST"

# Test Dashboard
Write-Host "DASHBOARD AND MONITORING" -ForegroundColor Magenta
Write-Host "─────────────────────" -ForegroundColor Magenta
Test-Endpoint "/dashboard/overview" "Dashboard Overview"
Test-Endpoint "/monitor" "System Monitoring"
Test-Endpoint "/analytics" "Analytics Data"

# Test Core Resources
Write-Host "ROUTERS & NETWORKS" -ForegroundColor Magenta
Write-Host "──────────────────" -ForegroundColor Magenta
Test-Endpoint "/routers" "List All Routers"
Test-Endpoint "/networks" "List All Networks"
Test-Endpoint "/devices" "List All Devices"
Test-Endpoint "/topology" "Network Topology"

# Test System Management
Write-Host "SYSTEM MANAGEMENT" -ForegroundColor Magenta
Write-Host "─────────────────" -ForegroundColor Magenta
Test-Endpoint "/logs" "System Logs"
Test-Endpoint "/notifications" "User Notifications"
Test-Endpoint "/reports" "Reports"

# Test Advanced Features
Write-Host "ADVANCED FEATURES" -ForegroundColor Magenta
Write-Host "─────────────────" -ForegroundColor Magenta
Test-Endpoint "/discovery" "Network Discovery"
Test-Endpoint "/security" "Security Settings"
Test-Endpoint "/traffic" "Traffic Analysis"
Test-Endpoint "/intrusion" "Intrusion Detection"
Test-Endpoint "/automation" "Automation Tasks"

Write-Host "═══════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "API Testing Complete" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════`n" -ForegroundColor Cyan
