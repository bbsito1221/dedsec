import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app("development")
    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
