from typing import NotRequired, TypedDict


class Usuario(TypedDict):
    id: NotRequired[int]
    nombre: str
    edad: NotRequired[int | None]
    activo: NotRequired[bool]


class UsuarioInvalidoError(Exception):
    """Se produce cuando un usuario contiene datos inválidos."""
    pass


def validar_usuario(usuario: Usuario) -> None:
    nombre = usuario.get("nombre")
    id_usuario = usuario.get("id")

    if nombre is None:
        raise UsuarioInvalidoError("El campo nombre es obligatorio")
    if not isinstance(nombre, str):
        raise UsuarioInvalidoError("El campo nombre debe ser texto")

    if id_usuario is not None and type(id_usuario) is not int:
        raise UsuarioInvalidoError("El campo id debe ser un entero")
    
    edad = usuario.get("edad")
    activo = usuario.get("activo")

    if edad is not None and type(edad) is not int:
        raise UsuarioInvalidoError("La edad debe ser un entero o None")

    if activo is not None and not isinstance(activo, bool):
        raise UsuarioInvalidoError("El campo activo debe ser booleano")

def es_usuario_valido(usuario: Usuario) -> bool:
    validar_usuario(usuario)

    edad = usuario.get("edad")
    activo = usuario.get("activo")

    return bool(activo and edad is not None and edad >= 18)

def procesar_usuarios(usuarios: list[Usuario]) -> list[str]:
    resultado = []

    for usuario in usuarios:
       if es_usuario_valido(usuario):
            resultado.append(usuario["nombre"])

    return resultado
