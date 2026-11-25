from tests.utils import get_token


def test_create_router(client):

    token = get_token(client)

    response = client.post(
        "/api/routers",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "name":"Main Router",
            "ip_address":"192.168.1.1"
        }
    )

    assert response.status_code == 201


def test_get_routers(client):

    token = get_token(client)

    response = client.get(
        "/api/routers",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200