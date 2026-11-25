def get_token(client):

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

    token = response.get_json()["access_token"]

    return token