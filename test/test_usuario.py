
def test_usuario_post(cliente, header):
    response = cliente.post('/api/v1/usuario', json={
        "NOMBRE": "David",
        "APELLIDO": None,
        "EDAD": 22,
        "CORREO": "david@gmail.com",
        "PASSWORD": "201940854"
        }, headers = header)
    assert response.status_code == 201
    assert response.json['IDUSUARIO'] == 2

def test_usuario_edit(cliente, header):
    response = cliente.put('/api/v1/usuario', json={
        "IDUSUARIO": 2,
        "NOMBRE": "David",
        "APELLIDO": "Perez",
        "EDAD": 25,
        "CORREO": "davidperez@gmail.com",
        "PASSWORD": "201940854"
        }, headers = header)
    assert response.status_code == 200
    assert response.json['IDUSUARIO'] == 2

def test_usuario_get_by_id(cliente, header):
    response = cliente.get('/api/v1/usuario/2', headers = header)
    assert response.status_code == 200
    assert response.json['IDUSUARIO'] == 2


