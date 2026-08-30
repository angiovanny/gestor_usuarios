from typing import NotRequired, TypedDict


class Usuario(TypedDict):
    id: NotRequired[int]
    nombre: str
    edad: NotRequired[int | None]
    activo: NotRequired[bool]


def es_usuario_valido(usuario: Usuario) -> bool:
    edad = usuario.get("edad")
    activo = usuario.get("activo")

    return bool(activo and edad is not None and edad >= 18)

def procesar_usuarios(usuarios: list[Usuario]) -> list[str]:
    resultado = []

    for usuario in usuarios:
       if es_usuario_valido(usuario):
            resultado.append(usuario["nombre"])

    return resultado
