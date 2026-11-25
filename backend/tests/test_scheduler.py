def test_scheduler(client):

    response = client.get(

        "/api/scheduler/jobs"

    )

    assert response.status_code == 200