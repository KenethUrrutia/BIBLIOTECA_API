
def test_estado(cliente, header):
    response = cliente.post('/api/v1/estado', json={
	    "NOMBRE": "Regular"
        }, headers = header)
    assert response.status_code == 201
    assert response.json['IDESTADO'] == 1

def test_estado_edit(cliente, header):
    response = cliente.put('/api/v1/estado', json={
        "IDESTADO": 1,
        "NOMBRE": "Nuevos"
        }, headers = header)
    assert response.status_code == 200
    assert response.json['IDESTADO'] == 1

def test_estado_get(cliente, header):
    response = cliente.get('/api/v1/estado', headers = header)
    assert response.status_code == 200

def test_estado_get_by_id(cliente, header):
    response = cliente.get('/api/v1/estado/1', headers = header)
    assert response.status_code == 200
    assert response.json['IDESTADO'] == 1

# def test_estado_delete(cliente, header):
#     response = cliente.delete('/api/v1/estado/1', headers = header)
#     assert response.status_code == 200

