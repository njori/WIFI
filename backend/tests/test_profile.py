def test_profile(client):

    response = client.get(

        "/api/profile"

    )

    assert response.status_code == 200