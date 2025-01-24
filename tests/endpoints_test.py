from fastapi.testclient import TestClient
from app.main import app
from app.config import settings


client = TestClient(app)


def test_get_queries():
    response = client.get('/queries')
    assert response.status_code == 200
    data = response.json()
    assert 'total' in data


def test_pagination():
    response = client.get('/queries?skip=0&limit=5')
    assert response.status_code == 200
    data = response.json()
    assert 'total' in data
    assert len(data['queries']) == 5

    response = client.get('/queries?skip=5&limit=5')
    assert response.status_code == 200
    data = response.json()
    assert 'total' in data
    assert len(data['queries']) == 5

    response = client.get('/queries?skip=10&limit=5')
    assert response.status_code == 200
    data = response.json()
    assert 'total' in data
    assert len(data['queries']) >= 5


def test_get_wallet_info():
    response = client.post('/wallet', params={'wallet_address': settings.address})
    assert response.status_code == 200
    data = response.json()
    assert 'wallet_address' in data
    assert data['wallet_address'] == settings.address