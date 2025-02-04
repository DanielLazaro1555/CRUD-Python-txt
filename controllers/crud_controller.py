# controllers/crud_controller.py

# Importamos las funciones necesarias para manejar los datos
from models.data_manager import agregar_dato, actualizar_dato, eliminar_dato, leer_datos


# ===============================
# Función para mostrar el menú principal
# ===============================
def mostrar_menu():
    """
    Muestra el menú principal del CRUD y gestiona la entrada del usuario.
    Permite navegar entre las opciones de ver, agregar, actualizar y eliminar registros.
    """
    while True:
        print("\n===== CRUD en Python con Archivos TXT =====")
        print("1. Ver registros")
        print("2. Agregar registro")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        # Opciones del menú
        if opcion == "1":
            ver_registros()
        elif opcion == "2":
            agregar_registro()
        elif opcion == "3":
            actualizar_registro()
        elif opcion == "4":
            eliminar_registro()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


# ===============================
# Función para ver registros
# ===============================
def ver_registros():
    """
    Muestra todos los registros almacenados en el archivo de texto.
    Si no hay registros, muestra un mensaje indicando que la lista está vacía.
    """
    datos = leer_datos()
    if not datos:
        print("No hay registros.")
        return

    print("\n===== Lista de Registros =====")
    for i, dato in enumerate(datos):
        print(f"{i}. Nombre: {dato['nombre']}, Edad: {dato['edad']}")


# ===============================
# Función para agregar un registro
# ===============================
def agregar_registro():
    """
    Solicita al usuario el nombre y la edad, y agrega un nuevo registro al archivo de datos.
    """
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    agregar_dato(nombre, edad)
    print("Registro agregado con éxito.")


# ===============================
# Función para actualizar un registro
# ===============================
def actualizar_registro():
    """
    Permite actualizar un registro existente seleccionándolo por su índice.
    El usuario debe ingresar el nuevo nombre y la nueva edad para el registro seleccionado.
    """
    ver_registros()  # Muestra los registros existentes para seleccionar uno
    try:
        indice = int(input("Ingrese el número del registro a actualizar: "))
        nombre = input("Nuevo nombre: ")
        edad = input("Nueva edad: ")
        if actualizar_dato(indice, nombre, edad):
            print("Registro actualizado con éxito.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Debe ingresar un número válido.")


# ===============================
# Función para eliminar un registro
# ===============================
def eliminar_registro():
    """
    Permite eliminar un registro del archivo de datos seleccionándolo por su índice.
    """
    ver_registros()  # Muestra los registros existentes para seleccionar uno
    try:
        indice = int(input("Ingrese el número del registro a eliminar: "))
        if eliminar_dato(indice):
            print("Registro eliminado con éxito.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Debe ingresar un número válido.")
