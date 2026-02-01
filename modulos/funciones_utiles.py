from modulos.validaciones import (
    validar_edad,
    validar_usuario,
    validar_email
)
from modulos.gestion_datos import (
    agregar_usuario,
    ROLES,
    buscar_usuario_por_nombre,
    eliminar_usuario_por_nombre,
    usuarios
)


# ──────────────── MENÚ ────────────────
def mostrar_menu():
    print("""
--- MENÚ PRINCIPAL (Elige una opción) ---
1. Agregar usuario
2. Listar usuarios
3. Buscar usuario por nombre
4. Eliminar usuario por nombre
5. Salir
""")


# ──────────────── AGREGAR USUARIO ────────────────
def agregar_usuario_menu():
    nombre = input("Ingrese nombre: ").strip()

    edad_input = input("Ingrese edad: ")
    if not edad_input.isdigit():
        print("Error: la edad debe ser un número entero.")
        return

    edad = int(edad_input)

    resultado_edad = validar_edad(edad)
    if not resultado_edad["valida"]:
        print(resultado_edad["mensaje"])
        return

    print(f"Categoría etaria: {resultado_edad['categoria']}")
    print(f"Roles disponibles: {ROLES}")

    rol_input = input("Ingrese rol: ")
    rol = rol_input.strip().lower().capitalize()

    if rol not in ROLES:
        print("Rol inválido.")
        return

    resultado_usuario = validar_usuario(rol.lower(), edad)
    if not resultado_usuario["valida"]:
        print(resultado_usuario["mensaje"])
        return

    email = input("Ingrese email: ").strip()

    resultado_email = validar_email(email)
    if not resultado_email["valida"]:
        print(resultado_email["mensaje"])
        return

    agregar_usuario(nombre, edad, rol, email)


# ──────────────── LISTAR USUARIOS ────────────────
def listar_usuarios_menu():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("\n--- LISTA DE USUARIOS ---")
    for usuario in usuarios:
        print(
            f"Nombre: {usuario.get('nombre')} | "
            f"Rol: {usuario.get('rol')} | "
            f"Correo: {usuario.get('email')}"
        )


# ──────────────── BUSCAR USUARIO ────────────────
def buscar_usuario_menu():
    nombre = input("Ingrese nombre a buscar: ").strip()
    usuario = buscar_usuario_por_nombre(nombre)

    if usuario:
        print("\nUsuario encontrado:")
        print(usuario)
    else:
        print("Usuario no encontrado.")


# ──────────────── ELIMINAR USUARIO ────────────────
def eliminar_usuario_menu():
    nombre = input("Ingrese nombre a eliminar: ").strip()
    eliminado = eliminar_usuario_por_nombre(nombre)

    if eliminado:
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario no existe.")


# ──────────────── EJECUCIÓN DEL SISTEMA ────────────────
def ejecutar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario_menu()
        elif opcion == "2":
            listar_usuarios_menu()
        elif opcion == "3":
            buscar_usuario_menu()
        elif opcion == "4":
            eliminar_usuario_menu()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")