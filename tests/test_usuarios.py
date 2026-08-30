from app.usuarios import Usuario, es_usuario_valido, procesar_usuarios


def test_unitario_menor_de_edad_no_es_incluido():
    usuarios: list[Usuario] = [
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
    usuarios: list[Usuario] = [
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
    usuarios: list[Usuario] = [
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
    usuarios: list[Usuario] = [
        {
            "id": 8,
            "nombre": "Carlos",
            "edad": 27
        }
    ]

    resultado = procesar_usuarios(usuarios)

    assert resultado == []

def test_procesar_varios_usuarios():
    usuarios: list[Usuario] = [
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

def test_usuario_activo_mayor_de_edad_es_valido():
    usuario:  Usuario = {
        "nombre": "Ana",
        "edad": 25,
        "activo": True
    }

    assert es_usuario_valido(usuario) is True

def test_usuario_menor_de_edad_no_es_valido():
    usuario: Usuario = {
        "nombre": "Pedro",
        "edad": 17,
        "activo": True
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_edad_none_no_es_valido():
    usuario: Usuario = {
        "nombre": "Diego",
        "edad": None,
        "activo": True
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_inactivo_no_es_valido():
    usuario: Usuario = {
        "nombre": "Martin",
        "edad": 26,
        "activo": False
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_activo_ausente_no_es_valido():
    usuario: Usuario = {
        "nombre": "Marcela",
        "edad": 30
    }

    assert es_usuario_valido(usuario) is False
