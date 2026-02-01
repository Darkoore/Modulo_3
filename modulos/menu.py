#Importaciones de funciones desde otros módulos
from modulos.validaciones import (
    validar_edad,
    validar_usuario,
    validar_email
)
from modulos.gestion_datos import (
    agregar_usuario,
    ROLES,
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

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # ──────────────── OPCIÓN 1 ────────────────
        if opcion == "1":
            nombre = input("Ingrese nombre: ").strip()

            edad_input = input("Ingrese edad: ")
            if not edad_input.isdigit():
                print("\nError: la edad debe ser un número entero.")
                continue

            edad = int(edad_input)

            resultado_edad = validar_edad(edad)
            if not resultado_edad["valida"]:
                print(resultado_edad["mensaje"])
                continue

            print(f"Categoría etaria: {resultado_edad['categoria']}")
            print(f"Roles disponibles: {ROLES}")

            rol_input = input("Ingrese rol: ")
            rol = rol_input.strip().lower().capitalize()

            if rol not in ROLES:
                print("\nRol inválido.")
                continue

            resultado_usuario = validar_usuario(rol.lower(), edad)
            if not resultado_usuario["valida"]:
                print(resultado_usuario["mensaje"])
                continue

            email = input("Ingrese email: ").strip()

            resultado_email = validar_email(email)
            if not resultado_email["valida"]:
                print(resultado_email["mensaje"])
                continue

            agregar_usuario(nombre, edad, rol, email)

        # ──────────────── OPCIÓN 2 ────────────────
        elif opcion == "2":
            if not usuarios:
                print("\nNo hay usuarios registrados.")
            else:
                print("\n--- LISTA DE USUARIOS ---")
                for usuario in usuarios:
                    print(
                        f"Nombre: {usuario.get('nombre')} | "
                        f"Rol: {usuario.get('rol')} | "
                        f"Correo: {usuario.get('email')}"
                    )

        # ──────────────── OPCIÓN 3 ────────────────
        elif opcion == "3":
            nombre_buscar = input("Ingrese nombre a buscar: ").strip().lower()
            encontrado = False

            for usuario in usuarios:
                if usuario.get("nombre", "").lower() == nombre_buscar:
                    print("\nUsuario encontrado:")
                    print(usuario)
                    encontrado = True
                    break

            if not encontrado:
                print("\nUsuario no encontrado.")

        # ──────────────── OPCIÓN 4 ────────────────
        elif opcion == "4":
            nombre_eliminar = input("Ingrese nombre a eliminar: ").strip().lower()
            eliminado = False

            for usuario in usuarios:
                if usuario.get("nombre", "").lower() == nombre_eliminar:
                    usuarios.remove(usuario)
                    print("\nUsuario eliminado correctamente.")
                    eliminado = True
                    break

            if not eliminado:
                print("\nUsuario no existe.")

        # ──────────────── OPCIÓN 5 ────────────────
        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")