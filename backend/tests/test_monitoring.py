def test_monitoring(client):

    response = client.get(

        "/api/monitoring/status"

    )

    assert response.status_code == 200