def test_prestamo(cliente, header):
    response = cliente.get('/api/v1/prestamo', headers = header)
    assert response.status_code == 200

def test_prestamo_post(cliente, header):
    response = cliente.post('/api/v1/prestamo', json={
        "PRESTAMO" : {
            "IDUSUARIO": 2,
            "IDLIBRO": 1,
            "FECHA_PRESTAMO": "2024-06-16T00:00:00",
            "FECHA_DEVOLUCION": None,
            "ESTADO": None,
            "IDESTADO": 1
            },
        "USUARIO" : {
            "IDUSUARIO": 1,
            "NOMBRE": "Ramiro",
            "APELLIDO": "Perez",
            "EDAD": 18,
            "CORREO": "ramiro@gmail.com"
        },
        "LIBRO" : {
            "IDLIBRO": 1,
            "IDGENERO": 1,
            "TITULO": "El Señor de los Anillos",
            "AUTOR": "Tolkien",
            "ANIO_PUBLICACION": "1954-01-01"
        },
        "ESTADO" : {
            "IDESTADO": 1,
            "NOMBRE": "Nuevos"
        }
        }, headers = header)
    assert response.status_code == 201
    assert response.json['IDPRESTAMO'] == 1