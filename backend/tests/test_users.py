def test_users(client):

    response = client.get(

        "/api/users"

    )

    assert response.status_code == 200