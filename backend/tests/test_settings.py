def test_settings(client):

    response = client.get(

        "/api/settings"

    )

    assert response.status_code == 200