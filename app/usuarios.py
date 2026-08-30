from typing import NotRequired, TypedDict


class Usuario(TypedDict):
    id: NotRequired[int]
    nombre: str
    edad: NotRequired[int | None]
    activo: NotRequired[bool]


class UsuarioInvalidoError(Exception):
    """Se produce cuando un usuario contiene datos inválidos."""
    pass


def es_usuario_valido(usuario: Usuario) -> bool:
    edad = usuario.get("edad")
    activo = usuario.get("activo")

    if edad is not None and type(edad) is not int:
        raise UsuarioInvalidoError("La edad debe ser un entero o None")

    if activo is not None and not isinstance(activo, bool):
        raise UsuarioInvalidoError("El campo activo debe ser booleano")

    return bool(activo and edad is not None and edad >= 18)

def procesar_usuarios(usuarios: list[Usuario]) -> list[str]:
    resultado = []

    for usuario in usuarios:
       if es_usuario_valido(usuario):
            resultado.append(usuario["nombre"])

    return resultado
