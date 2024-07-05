def test_genero(cliente, header):
    response = cliente.get('/api/v1/genero', headers = header)
    assert response.status_code == 200

def test_genero_post(cliente, header):
    response = cliente.post('/api/v1/genero', json={
        "NOMBRE": "Accion"
        }, headers = header)
    assert response.status_code == 201
    assert response.json['IDGENERO'] == 1

def test_genero_edit(cliente, header):
    response = cliente.put('/api/v1/genero', json={
        "IDGENERO": 1,
        "NOMBRE": "Aventura"
        }, headers = header)
    assert response.status_code == 200
    assert response.json['IDGENERO'] == 1

def test_genero_get_by_id(cliente, header):
    response = cliente.get('/api/v1/genero/1', headers = header)
    assert response.status_code == 200
    assert response.json['IDGENERO'] == 1

# def test_genero_delete(cliente, header):
#     response = cliente.delete('/api/v1/genero/1', headers = header)
#     assert response.status_code == 200

