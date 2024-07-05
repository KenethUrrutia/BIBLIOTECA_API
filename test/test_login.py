from app import app

def test_login():
    client = app.test_client()

    response = client.post('/api/v1/login', json={
        "CORREO" : "ramiro@gmail.com",
        "PASSWORD" : "201940854" 
        })
    assert response.status_code == 200