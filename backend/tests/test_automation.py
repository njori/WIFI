def test_automation(client):

    response = client.get(

        "/api/automation"

    )

    assert response.status_code == 200