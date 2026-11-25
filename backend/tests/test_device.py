from tests.utils import get_token


def test_devices(client):

    token = get_token(client)

    response = client.get(
        "/api/devices",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code == 200