def procesar_usuarios(usuarios: list[dict]) -> list[str]:
    resultado = []

    for usuario in usuarios:
        edad = usuario.get("edad")
        activo = usuario.get("activo") 

        if activo and edad and edad >= 18:
            resultado.append(usuario["nombre"])

    return resultado
