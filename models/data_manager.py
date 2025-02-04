# models/data_manager.py

import os  # Módulo para interactuar con el sistema de archivos

# ===============================
# Ruta del archivo donde se almacenarán los datos
# ===============================
FILE_PATH = "datos.txt"


# ===============================
# Función para leer los datos desde el archivo
# ===============================
def leer_datos():
    """
    Lee los datos almacenados en el archivo 'datos.txt' y devuelve una lista de diccionarios.
    Cada línea del archivo representa un registro con el formato: nombre,edad

    :return: Lista de diccionarios con los datos leídos
    """
    if not os.path.exists(FILE_PATH):
        return []  # Si el archivo no existe, devuelve una lista vacía

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Lee todas las líneas del archivo

    datos = []
    for line in lines:
        # Separa el nombre y la edad por la coma
        nombre, edad = line.strip().split(",")
        # Crea un diccionario para cada registro
        datos.append({"nombre": nombre, "edad": edad})
    return datos


# ===============================
# Función para escribir datos en el archivo
# ===============================
def escribir_datos(datos):
    """
    Escribe la lista de datos en el archivo 'datos.txt'.
    Sobrescribe el archivo con el contenido actualizado.

    :param datos: Lista de diccionarios con los datos a guardar
    """
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for dato in datos:
            # Guarda cada registro en una nueva línea
            file.write(f"{dato['nombre']},{dato['edad']}\n")


# ===============================
# Función para agregar un nuevo dato
# ===============================
def agregar_dato(nombre, edad):
    """
    Agrega un nuevo registro al archivo 'datos.txt'.

    :param nombre: Nombre de la persona
    :param edad: Edad de la persona
    """
    datos = leer_datos()  # Obtiene los datos existentes
    datos.append({"nombre": nombre, "edad": edad})  # Agrega el nuevo registro
    escribir_datos(datos)  # Guarda los datos actualizados en el archivo


# ===============================
# Función para actualizar un dato existente
# ===============================
def actualizar_dato(indice, nombre, edad):
    """
    Actualiza un registro existente en el archivo 'datos.txt' usando su índice.

    :param indice: Índice del registro que se desea actualizar
    :param nombre: Nuevo nombre para el registro
    :param edad: Nueva edad para el registro
    :return: True si la actualización fue exitosa, False si el índice es inválido
    """
    datos = leer_datos()
    if 0 <= indice < len(datos):  # Verifica que el índice sea válido
        # Actualiza el registro
        datos[indice] = {"nombre": nombre, "edad": edad}
        escribir_datos(datos)  # Guarda los cambios
        return True
    return False  # Retorna False si el índice es inválido


# ===============================
# Función para eliminar un dato existente
# ===============================
def eliminar_dato(indice):
    """
    Elimina un registro del archivo 'datos.txt' usando su índice.

    :param indice: Índice del registro que se desea eliminar
    :return: True si la eliminación fue exitosa, False si el índice es inválido
    """
    datos = leer_datos()
    if 0 <= indice < len(datos):  # Verifica que el índice sea válido
        del datos[indice]  # Elimina el registro
        escribir_datos(datos)  # Guarda los cambios
        return True
    return False  # Retorna False si el índice es inválido
