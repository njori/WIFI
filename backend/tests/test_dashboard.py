from tests.utils import get_token


def test_dashboard(client):

    token = get_token(client)

    response = client.get(
        "/api/dashboard/overview",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code == 200