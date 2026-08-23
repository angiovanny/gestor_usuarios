def procesar_usuarios(usuarios: list[dict]) -> list[str]:
    resultado = []

    for usuario in usuarios:
        edad = usuario.get("edad")

        if usuario["activo"] and edad and edad >= 18:
            resultado.append(usuario["nombre"])

    return resultado