# Módulo para validaciones de usuario y edad
def validar_usuario(tipo_usuario, edad):
    if tipo_usuario == "admin":
        if edad >= 18:
            return {
                "valida": True,
                "mensaje": "\nAdmin autorizado",
                "rol": "admin"
            }
        else:
            return {
                "valida": False,
                "mensaje": "\nAdmin NO autorizado (menor de edad)",
                "rol": None
            }

    return {
        "valida": True,
        "mensaje": "Usuario estándar",
        "rol": "usuario"
    }

def validar_edad(edad):
    if edad < 0:
        return {
            "valida": False,
            "mensaje": "\nEdad inválida",
            "categoria": None
        }

    if edad < 18:
        categoria = "menor de edad"
    elif edad <= 60:
        categoria = "adulto"
    else:
        categoria = "adulto mayor"

    return {
        "valida": True,
        "mensaje": "\nEdad válida",
        "categoria": categoria
    }