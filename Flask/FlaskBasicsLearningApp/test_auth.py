import pytest 

from flask import current_app
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"
        yield client

def test_register_page(client):
    response = client.get('/')
    print("response.data", response.data)
    assert response.status_code == 200
    assert b'<h1>Hello world from main blueprint</h1>' in response.data
