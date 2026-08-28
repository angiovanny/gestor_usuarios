from app.usuarios import procesar_usuarios


def test_unitario_menor_de_edad_no_es_incluido():
    usuarios = [
        {
            "id": 5,
            "nombre": "Juan",
            "edad": 16,
            "activo": True
        }
    ]

    resultado = procesar_usuarios(usuarios)

    assert resultado == []

def test_usuario_edad_none():
    usuarios = [
        {
            "id": 6,
            "nombre": "Laura",
            "edad": None,
            "activo": True
        }
    ]

    resultado = procesar_usuarios(usuarios)

    assert resultado == []

def test_usuario_activo_mayor_de_edad_es_incluido():
    usuarios = [
        {
            "id": 1,
            "nombre": "Ana",
            "edad": 25,
            "activo": True
        }
    ]

    resultado = procesar_usuarios(usuarios)

    assert resultado == ["Ana"]

def test_usuario_activo_ausente():
    usuarios = [
        {
            "id": 8,
            "nombre": "Carlos",
            "edad": 27
        }
    ]

    resultado = procesar_usuarios(usuarios)

    assert resultado == []

def test_procesar_varios_usuarios():
    usuarios = [
        {
            "nombre": "Ana", 
            "edad": 25, 
            "activo": True
        },
        {
            "nombre": "Pedro", 
            "edad": 17, 
            "activo": True
        },
        {
            "nombre": "Laura", 
            "edad": None, 
            "activo": True}
        ,
        {
            "nombre": "Carlos", 
            "edad": 27
        },
        {
            "nombre": "Marta", 
            "edad": 30, 
            "activo": False
        }
    ]

    resultado = procesar_usuarios(usuarios)
    
    assert resultado == ["Ana"]
