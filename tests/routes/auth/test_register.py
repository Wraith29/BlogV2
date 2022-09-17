from flask.testing import FlaskClient


def test_register_index(client: FlaskClient) -> None:
    response = client.get("/auth/register/")
    print(response)
