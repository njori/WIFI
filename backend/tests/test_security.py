def test_security(client):

    response = client.get(

        "/api/security/settings"

    )

    assert response.status_code == 200