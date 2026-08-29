from typing import NotRequired, TypedDict


class Usuario(TypedDict):
    id: NotRequired[int]
    nombre: str
    edad: NotRequired[int | None]
    activo: NotRequired[bool]


def procesar_usuarios(usuarios: list[Usuario]) -> list[str]:
    resultado = []

    for usuario in usuarios:
        edad = usuario.get("edad")
        activo = usuario.get("activo") 

        if activo and edad and edad >= 18:
            resultado.append(usuario["nombre"])

    return resultado
