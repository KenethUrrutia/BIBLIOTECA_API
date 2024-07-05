def test_libro(cliente, header):
    response = cliente.get('/api/v1/libro', headers = header)
    assert response.status_code == 200

def test_libro_post(cliente, header):
    response = cliente.post('/api/v1/libro', json={
        "IDGENERO": 1,
        "TITULO": "El señor de los anillos",
        "AUTOR": "J.R.R. Tolkien",
        "ANIO_PUBLICACION": "1954-01-01"
        }, headers = header)
    assert response.status_code == 201
    assert response.json['IDLIBRO'] == 1

def test_libro_edit(cliente, header):
    response = cliente.put('/api/v1/libro', json={
        "IDLIBRO": 1,
        "IDGENERO": 1,
        "TITULO": "El Señor de los Anillos",
        "AUTOR": "Tolkien",
        "ANIO_PUBLICACION": "1954-01-01"
        }, headers = header)
    assert response.status_code == 200
    assert response.json['IDLIBRO'] == 1

def test_libro_get_by_id(cliente, header):
    response = cliente.get('/api/v1/libro/1', headers = header)
    assert response.status_code == 200
    assert response.json['IDLIBRO'] == 1

# def test_libro_delete(cliente, header):
#     response = cliente.delete('/api/v1/libro/1', headers = header)
#     assert response.status_code == 200



