from tests.utils import get_token


def test_networks(client):

    token = get_token(client)

    response = client.get(
        "/api/networks",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code == 200