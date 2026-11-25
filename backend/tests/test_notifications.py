from tests.utils import get_token


def test_notifications(client):

    token = get_token(client)

    response = client.get(
        "/api/notifications",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code == 200