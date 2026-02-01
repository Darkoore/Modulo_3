# Datos inmutables para roles del sistema
ROLES = ("Admin", "Usuario", "Invitado")

# Lista de usuarios
usuarios = []

# Set para evitar correos duplicados
correos_registrados = set()


def agregar_usuario(nombre, edad, rol, email):
    # Validar rol usando tupla
    if rol not in ROLES:
        print("\nRol inválido.")
        return

    # Evitar correos duplicados usando set
    if email in correos_registrados:
        print("\nError: correo ya registrado.")
        return

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "rol": rol,
        "email": email
    }

    # append(): agregar a la lista
    usuarios.append(usuario)

    # agregar correo al set
    correos_registrados.add(email)

    print("\nUsuario agregado correctamente.")


def listar_usuarios():
    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    print("\n--- LISTA DE USUARIOS ---")
    for usuario in usuarios:
        print(
            usuario.get("nombre"),  # Uso de dict.get()
            "-",
            usuario.get("rol"),
            "-",
            usuario.get("email")
        )


def buscar_usuario_por_nombre(nombre):
    for usuario in usuarios:
        if usuario.get("nombre", "").lower() == nombre.lower():
            return usuario
    return None


def eliminar_usuario_por_nombre(nombre):
    for usuario in usuarios:
        if usuario.get("nombre", "").lower() == nombre.lower():
            usuarios.remove(usuario)
            correos_registrados.remove(usuario["email"])
            return True
    return False


# Función demostrativa para uso académico
# Permite mostrar claves y valores de un usuario (dict.keys / dict.values)
def mostrar_claves_y_valores(nombre):
    usuario = buscar_usuario_por_nombre(nombre)

    if not usuario:
        print("Usuario no existe.")
        return

    print("\nClaves del usuario:")
    print(usuario.keys()) # Uso de dict.keys()

    print("\nValores del usuario:")
    print(usuario.values()) # Uso de dict.values()