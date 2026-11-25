from tests.utils import get_token


def test_reports(client):

    token = get_token(client)

    response = client.get(
        "/api/reports",
        headers={
            "Authorization":f"Bearer {token}"
        }
    )

    assert response.status_code == 200