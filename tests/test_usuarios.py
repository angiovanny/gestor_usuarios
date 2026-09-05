from typing import cast

import pytest

from app.usuarios import (
    Usuario,
    UsuarioInvalidoError,
    edad_valida,
    es_usuario_valido,
    procesar_usuarios,
    usuario_activo,
    validar_usuario,
)


def test_unitario_menor_de_edad_no_es_incluido() -> None:
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

def test_usuario_edad_none() -> None:
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

def test_usuario_activo_mayor_de_edad_es_incluido() -> None:
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

def test_usuario_activo_ausente() -> None:
    usuarios: list[Usuario] = [
        {
            "id": 8,
            "nombre": "Carlos",
            "edad": 27
        }
    ]

    resultado = procesar_usuarios(usuarios)

    assert resultado == []

def test_procesar_varios_usuarios() -> None:
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

def test_usuario_activo_mayor_de_edad_es_valido() -> None:
    usuario:  Usuario = {
        "nombre": "Ana",
        "edad": 25,
        "activo": True
    }

    assert es_usuario_valido(usuario) is True

def test_usuario_menor_de_edad_no_es_valido() -> None:
    usuario: Usuario = {
        "nombre": "Pedro",
        "edad": 17,
        "activo": True
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_edad_none_no_es_valido() -> None:
    usuario: Usuario = {
        "nombre": "Diego",
        "edad": None,
        "activo": True
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_inactivo_no_es_valido() -> None:
    usuario: Usuario = {
        "nombre": "Martin",
        "edad": 26,
        "activo": False
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_activo_ausente_no_es_valido() -> None:
    usuario: Usuario = {
        "nombre": "Marcela",
        "edad": 30
    }

    assert es_usuario_valido(usuario) is False

def test_edad_con_tipo_incorrecto() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Pedro",
            "edad": "diecisiete",
            "activo": True
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        es_usuario_valido(usuario)

def test_activo_con_tipo_incorrecto() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Diego",
            "edad": 30,
            "activo": "si"
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        es_usuario_valido(usuario)

def test_edad_boolean_no_es_valida() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Carlos",
            "edad": True,
            "activo": True
        }
    )
    with pytest.raises(UsuarioInvalidoError):
        es_usuario_valido(usuario)

def test_validar_usuario_con_datos_correctos() -> None:
    usuario: Usuario = {
        "nombre": "Ana",
        "edad": 25,
        "activo": True
    }

    validar_usuario(usuario)

def test_validar_usuario_edad_incorrecta() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Pedro",
            "edad": "diecisiete",
            "activo": True
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_validar_usuario_activo_incorrecto() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Diego",
            "edad": 30,
            "activo": "si"
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_es_usuario_valido_rechaza_datos_invalidos() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Pedro",
            "edad": "diecisiete",
            "activo": True
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        es_usuario_valido(usuario)

def test_usuario_sin_nombre_no_es_valido() -> None:
    usuario = cast(
        Usuario,
        {
            "edad": 25,
            "activo": True
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_nombre_con_tipo_invalido_no_es_valido() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": 123
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_id_con_tipo_invalido_no_es_valido() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Andres",
            "id": "123"
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_id_booleano_no_es_valido() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Andres",
            "id": True
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_id_entero_es_valido() -> None:
    usuario: Usuario = {
        "nombre": "Andres",
        "id": 123
    }

    validar_usuario(usuario)

def test_edad_none_es_valida() -> None:
    usuario: Usuario = {
            "nombre": "Andres",
            "edad": None
    }

    validar_usuario(usuario)

def test_activo_con_tipo_invalido_no_es_valido() -> None:
    usuario = cast(
        Usuario,
        {
            "nombre": "Andres",
            "activo": "True"
        }
    )

    with pytest.raises(UsuarioInvalidoError):
        validar_usuario(usuario)

def test_activo_booleano_es_valido() -> None:
    usuario: Usuario = {
            "nombre": "Andres",
            "activo": True
    }

    validar_usuario(usuario)

def test_usuario_solo_con_nombre_es_valido_estructuralmente() -> None:
    usuario: Usuario = {
        "nombre": "Andres"
    }

    validar_usuario(usuario)

def test_usuario_menor_de_18_no_es_valido() -> None:
    usuario: Usuario = {
        "nombre": "Pedro",
        "edad": 16,
        "activo": True
    }

    assert es_usuario_valido(usuario) is False

def test_usuario_con_18_anos_es_valida() -> None:
    usuario: Usuario = {
        "nombre": "Pedro",
        "edad": 18,
        "activo": True
    }

    assert es_usuario_valido(usuario) is True

def test_usuario_mayor_de_18_es_valida() -> None:
    usuario: Usuario = {
        "nombre": "Pedro",
        "edad": 25,
        "activo": True
    }

    assert es_usuario_valido(usuario) is True

def test_edad_none_no_es_valida() -> None:
    assert edad_valida(None) is False

def test_edad_menor_de_18_no_es_valida() -> None:
    assert edad_valida(16) is False

def test_edad_de_18_es_valida() -> None:
    assert edad_valida(18) is True

def test_edad_mayor_de_18_es_valida() -> None:
    assert edad_valida(25) is True

def test_usuario_activo_es_valido() -> None:
    assert usuario_activo(True) is True

def test_activo_false_no_es_valido() -> None:
    assert usuario_activo(False) is False
