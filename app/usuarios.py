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

    if not nombre_valido(nombre):
        raise UsuarioInvalidoError("El nombre no puede estar vacio")

    if not usuario_id_valido(id_usuario):
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

    return bool(usuario_activo(activo) and edad_valida(edad))


def edad_valida(edad: int | None) -> bool:
    return edad is not None and edad >= 18


def usuario_activo(activo: bool | None) -> bool:
    return activo is True


def usuario_id_valido(id_usuario: int | None) -> bool:
    return id_usuario is None or type(id_usuario) is int


def nombre_valido(nombre: str) -> bool:
    return nombre.strip() != ""


def procesar_usuarios(usuarios: list[Usuario]) -> list[str]:
    resultado = []

    for usuario in usuarios:
       if es_usuario_valido(usuario):
            resultado.append(usuario["nombre"])

    return resultado
