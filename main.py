# Importar funciones de validación
from modulos.validaciones import validar_edad, validar_usuario

# Entrada de datos
nombre = input("Ingrese su nombre: ")

edad_input = input("Ingrese su edad: ")

# Gestión de errores con validaciones condicionales
if not edad_input.isdigit():
    print("Error: la edad debe ser un número entero")
else:
    edad = int(edad_input)
    tipo_usuario = input("Ingrese tipo de usuario (admin / normal): ")

    # Validaciones
    categoria = validar_edad(edad)
    estado_usuario = validar_usuario(tipo_usuario, edad)

    # Salida
    print("\n--- RESULTADOS ---")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Categoría:", categoria)
    print("Estado del usuario:", estado_usuario)