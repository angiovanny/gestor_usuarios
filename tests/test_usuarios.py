from typing import cast

import pytest

from app.usuarios import (
    Usuario,
    UsuarioInvalidoError,
    es_usuario_valido,
    procesar_usuarios,
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
