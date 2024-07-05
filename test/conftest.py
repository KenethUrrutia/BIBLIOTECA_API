import pytest
from app import app

@pytest.fixture()
def cliente():
    cliente = app.test_client()
    yield cliente


@pytest.fixture()
def header(cliente):
    response = cliente.post('/api/v1/login', json={
        "CORREO" : "ramiro@gmail.com",
        "PASSWORD" : "201940854" 
        })
    token = response.json['token']
    header = {"Authorization" : f"Bearer {token}"}
    yield header

