# views/app_view.py

import tkinter as tk
from tkinter import messagebox, ttk
from models.data_manager import agregar_dato, leer_datos, actualizar_dato, eliminar_dato

# ===============================
# Configuración de estilos
# ===============================
BG_COLOR = "#f4f4f4"      # Color de fondo de la ventana
BTN_COLOR = "#4CAF50"     # Color de los botones
BTN_HOVER = "#45a049"     # Color de los botones al pasar el mouse
FONT = ("Arial", 12)      # Fuente predeterminada para los textos


# ===============================
# Función para agregar un registro
# ===============================
def agregar_registro(nombre, edad, lista):
    """
    Agrega un nuevo registro al archivo de datos y actualiza la vista.

    :param nombre: Nombre de la persona
    :param edad: Edad de la persona
    :param lista: Widget Treeview para mostrar los registros
    """
    if nombre and edad:
        agregar_dato(nombre, edad)  # Guarda el dato en el archivo de texto
        messagebox.showinfo("Éxito", "Registro agregado correctamente.")
        mostrar_registros(lista)    # Refresca la lista de registros
    else:
        messagebox.showwarning("Error", "Completa todos los campos.")


# ===============================
# Función para actualizar un registro
# ===============================
def actualizar_registro(indice, nombre, edad, lista):
    """
    Actualiza un registro existente en el archivo de datos.

    :param indice: Índice del registro a actualizar
    :param nombre: Nuevo nombre
    :param edad: Nueva edad
    :param lista: Widget Treeview para mostrar los registros actualizados
    """
    if actualizar_dato(indice, nombre, edad):
        messagebox.showinfo("Éxito", "Registro actualizado.")
        mostrar_registros(lista)
    else:
        messagebox.showerror("Error", "Selecciona un registro válido.")


# ===============================
# Función para eliminar un registro
# ===============================
def eliminar_registro(indice, lista):
    """
    Elimina un registro del archivo de datos.

    :param indice: Índice del registro a eliminar
    :param lista: Widget Treeview para mostrar los registros actualizados
    """
    if eliminar_dato(indice):
        messagebox.showinfo("Éxito", "Registro eliminado.")
        mostrar_registros(lista)
    else:
        messagebox.showerror("Error", "Selecciona un registro válido.")


# ===============================
# Función para mostrar todos los registros
# ===============================
def mostrar_registros(lista):
    """
    Muestra todos los registros en el widget Treeview.

    :param lista: Widget Treeview donde se mostrarán los registros
    """
    lista.delete(*lista.get_children())  # Limpia la lista actual
    datos = leer_datos()                 # Obtiene los datos del archivo
    for i, dato in enumerate(datos):
        lista.insert("", "end", values=(i, dato['nombre'], dato['edad']))


# ===============================
# Función principal para crear la interfaz gráfica
# ===============================
def crear_interfaz():
    """
    Crea la interfaz gráfica para el CRUD usando Tkinter.
    """
    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("CRUD en Python")
    ventana.geometry("500x400")
    ventana.configure(bg=BG_COLOR)

    # =========== Frame para el formulario ===========
    frame_formulario = tk.Frame(ventana, bg=BG_COLOR)
    frame_formulario.pack(pady=10)

    # Etiqueta y campo de entrada para el nombre
    tk.Label(frame_formulario, text="Nombre:", bg=BG_COLOR,
             font=FONT).grid(row=0, column=0, padx=5, pady=5)
    nombre_entry = tk.Entry(frame_formulario, font=FONT)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta y campo de entrada para la edad
    tk.Label(frame_formulario, text="Edad:", bg=BG_COLOR,
             font=FONT).grid(row=1, column=0, padx=5, pady=5)
    edad_entry = tk.Entry(frame_formulario, font=FONT)
    edad_entry.grid(row=1, column=1, padx=5, pady=5)

    # =========== Estilo para los botones ===========
    def estilo_boton(boton):
        """
        Aplica un estilo personalizado a los botones.
        """
        boton.configure(bg=BTN_COLOR, fg="white", relief="flat",
                        activebackground=BTN_HOVER, padx=10, pady=5)

    # =========== Botones de acción ===========
    # Botón para agregar registros
    btn_agregar = tk.Button(ventana, text="Agregar", command=lambda: agregar_registro(
        nombre_entry.get(), edad_entry.get(), lista_registros))
    estilo_boton(btn_agregar)
    btn_agregar.pack(pady=5)

    # Botón para actualizar registros
    btn_actualizar = tk.Button(ventana, text="Actualizar", command=lambda: actualizar_registro(
        lista_registros.selection()[0], nombre_entry.get(), edad_entry.get(), lista_registros))
    estilo_boton(btn_actualizar)
    btn_actualizar.pack(pady=5)

    # Botón para eliminar registros
    btn_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: eliminar_registro(
        lista_registros.selection()[0], lista_registros))
    estilo_boton(btn_eliminar)
    btn_eliminar.pack(pady=5)

    # =========== Tabla para mostrar registros ===========
    columns = ("ID", "Nombre", "Edad")  # Columnas de la tabla
    lista_registros = ttk.Treeview(ventana, columns=columns, show="headings")
    lista_registros.heading("ID", text="ID")
    lista_registros.heading("Nombre", text="Nombre")
    lista_registros.heading("Edad", text="Edad")
    lista_registros.pack(pady=10, fill="x", padx=20)

    # Mostrar registros existentes al iniciar la app
    mostrar_registros(lista_registros)

    # Inicia el bucle principal de la aplicación
    ventana.mainloop()
