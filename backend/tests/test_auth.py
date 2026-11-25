def test_register(client):

    response = client.post(
        "/api/auth/register",
        json={
            "username":"admin",
            "email":"admin@test.com",
            "password":"12345678",
            "first_name":"Admin",
            "last_name":"User"
        }
    )

    assert response.status_code == 201


def test_login(client):

    client.post(
        "/api/auth/register",
        json={
            "username":"admin",
            "email":"admin@test.com",
            "password":"12345678",
            "first_name":"Admin",
            "last_name":"User"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "email":"admin@test.com",
            "password":"12345678"
        }
    )

    assert response.status_code == 200

    assert "access_token" in response.get_json()