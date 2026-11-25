from tests.utils import get_token


def test_logs(client):

    token = get_token(client)

    response = client.get(
        "/api/logs",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code == 200