import tkinter as tk
from tkinter import font, ttk, messagebox
import pyodbc


# Conexión a la base de datos
def conectar_bd():
    try:
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=ARJONA_29\\SQLEXPRESS;"
            "DATABASE=SistemaDeRiego;"
            "Trusted_Connection=yes;"
        )
        cursor = connection.cursor()
        print("Conexión exitosa a la base de datos")
        return connection, cursor
    except Exception as ex:
        messagebox.showerror("Error", f"Error en la conexión: {ex}")
        return None, None


# Ventana Login
def login(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Login")
    root.geometry("300x500")
    root.resizable(False, False)
    root.configure(bg="white")

    # Crear el formulario de inicio de sesión
    title_font = font.Font(family="Arial", size=20, weight="bold")
    title_label = tk.Label(root, text="AGROAPP", font=title_font, fg="green", bg="white")
    title_label.place(relx=0.5, rely=0.2, anchor="center")

    form_frame = tk.Frame(root, bg="white", highlightbackground="green", highlightthickness=1, pady=20)
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=250)

    email_label = tk.Label(form_frame, text="Correo electrónico o usuario", bg="white", fg="gray")
    email_label.pack(pady=(10, 0), anchor="w")
    email_entry = tk.Entry(form_frame, bg="#f4f4f4", relief="flat", width=30)
    email_entry.pack(pady=(0, 10), padx=10)

    password_label = tk.Label(form_frame, text="Contraseña", bg="white", fg="gray")
    password_label.pack(pady=(10, 0), anchor="w")
    password_entry = tk.Entry(form_frame, show="*", bg="#f4f4f4", relief="flat", width=30)
    password_entry.pack(pady=(0, 10), padx=10)

    # Función para validar las credenciales
    def validar_credenciales():
        usuario_email = email_entry.get()
        contrasena = password_entry.get()

        try:
            # Consulta SQL para verificar las credenciales
            query = """
            SELECT COUNT(*) 
            FROM Usuarios 
            WHERE (Nombre = ? OR Correo = ?) AND Contraseña = ?
            """
            cursor.execute(query, (usuario_email, usuario_email, contrasena))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                # Si las credenciales son válidas, pasar a la ventana de sistema de riego
                sistema_de_riego(root)
            else:
                # Mostrar un mensaje de error
                tk.messagebox.showerror("Error", "Credenciales incorrectas. Inténtalo de nuevo.")
        except Exception as ex:
            tk.messagebox.showerror("Error", f"Error al validar las credenciales: {ex}")

    # Botón de acceso
    access_button = tk.Button(form_frame,text="Acceso",bg="green",fg="white",relief="flat",width=20,height=1,command=validar_credenciales,)
    access_button.pack(pady=(10, 0))

   
# Ventana Sistema de Riego
def sistema_de_riego(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Sistema de Riego")
    root.geometry("300x500")
    root.resizable(False, False)
    root.configure(bg="white")

    # Botones superiores
    menu_button = tk.Menubutton(root, text="⋮", font=("Arial", 12), bg="green", fg="white", relief="flat")
    menu = tk.Menu(menu_button, tearoff=0)
    menu.add_command(label="Chatbot", command=lambda: chatbot(root))
    menu.add_command(label="Cerrar Sesión", command=root.quit)
    menu_button.config(menu=menu)
    menu_button.place(x=260, y=10)

    # Título
    title_font = font.Font(family="Arial", size=16, weight="bold")
    title_label = tk.Label(root, text="SISTEMA DE RIEGO", font=title_font, fg="white", bg="green")
    title_label.place(relx=0.5, rely=0.15, anchor="center")

    # Campos y switches
    fields = ["Campo 1", "Campo 2", "Campo 3", "Campo 4"]
    switches = {}

    for i, field in enumerate(fields):
        field_label = tk.Label(root, text=field, bg="white", fg="black")
        field_label.place(x=50, y=150 + (i * 50))
        switch = ttk.Checkbutton(root, text="Activar/Desactivar")
        switch.place(x=150, y=150 + (i * 50))
        switches[field] = switch

    # Actualizar estados de riego
    def actualizar_riego():
        for field, switch in switches.items():
            estado = switch.instate(["selected"])
            print(f"{field}: {'Activo' if estado else 'Inactivo'}")

    actualizar_button = tk.Button(root, text="Actualizar", command=actualizar_riego, bg="green", fg="white")
    actualizar_button.place(relx=0.5, rely=0.8, anchor="center")

#Ventana del chatbot
def chatbot(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Chatbot")
    root.geometry("300x500")
    root.resizable(False, False)
    root.configure(bg="white")

    # Botones superiores
    menu_button = tk.Menubutton(root, text="⋮", font=("Arial", 12), bg="green", fg="white", relief="flat")
    menu = tk.Menu(menu_button, tearoff=0)
    menu.add_command(label="Sistema de Riego", command=lambda: sistema_de_riego(root))
    menu.add_command(label="Cerrar Sesión", command=root.quit)
    menu_button.config(menu=menu)
    menu_button.place(x=260, y=10)

    # Título
    title_font = font.Font(family="Arial", size=16, weight="bold")
    title_label = tk.Label(root, text="CHATBOT", font=title_font, fg="white", bg="green")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Área de chat
    chat_frame = tk.Frame(root, bg="white")
    chat_frame.place(relx=0.5, rely=0.5, anchor="center", width=280, height=350)

    chat_display = tk.Text(chat_frame, state="disabled", bg="#f4f4f4", wrap="word", relief="flat", height=15)
    chat_display.pack(pady=10, fill=tk.BOTH)

    # Área de entrada y envío
    input_frame = tk.Frame(root, bg="white")
    input_frame.place(relx=0.5, rely=0.9, anchor="center", width=280, height=50)

    chat_entry = tk.Entry(input_frame, bg="#f4f4f4", relief="flat", width=30)
    chat_entry.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

    enviar_button = tk.Button(input_frame, text="Enviar", command=lambda: enviar_mensaje(), bg="green", fg="white")
    enviar_button.pack(side=tk.RIGHT, padx=5, pady=5)

    # Opciones iniciales
    def mostrar_opciones():
        chat_display.config(state="normal")
        opciones = """
Bot: Estas son algunas preguntas que puedes hacerme:
1. ¿Cuál es el estado de los campos?
2. ¿Qué recomendaciones hay para el cultivo?
3. Información sobre enfermedades.
4. Información sobre plagas.
5. Compatibilidad de cultivos.
6. ¿Qué etapas tiene el cultivo de papa?
Por favor, escribe tu pregunta o el número correspondiente.
"""
        chat_display.insert(tk.END, opciones)
        chat_display.config(state="disabled")

    mostrar_opciones()

    # Consultas dinámicas
    def procesar_mensaje(mensaje):
        mensaje = mensaje.lower()
        chat_display.config(state="normal")

        if "estado de los campos" in mensaje or mensaje == "1":
            try:
                cursor.execute("SELECT Nombre_Campo, Tipo_Cultivo FROM dbo.Campos_Informacion")
                resultados = cursor.fetchall()
                if resultados:
                    chat_display.insert(tk.END, "Bot: Aquí está el estado de los campos:\n")
                    for campo in resultados:
                        chat_display.insert(tk.END, f"- {campo[0]} con cultivo: {campo[1]}\n")
                else:
                    chat_display.insert(tk.END, "Bot: No hay información sobre los campos.\n")
            except Exception as ex:
                chat_display.insert(tk.END, f"Bot: Error al obtener información: {ex}\n")

        elif "recomendaciones" in mensaje or mensaje == "2":
            try:
                cursor.execute("SELECT Recomendacion FROM dbo.Recomendaciones")
                recomendaciones = cursor.fetchall()
                if recomendaciones:
                    chat_display.insert(tk.END, "Bot: Estas son las recomendaciones:\n")
                    for rec in recomendaciones:
                        chat_display.insert(tk.END, f"- {rec[0]}\n")
                else:
                    chat_display.insert(tk.END, "Bot: No hay recomendaciones disponibles.\n")
            except Exception as ex:
                chat_display.insert(tk.END, f"Bot: Error al obtener recomendaciones: {ex}\n")

        elif "enfermedades" in mensaje or mensaje == "3":
            try:
                cursor.execute("SELECT Enfermedad, Descripcion FROM dbo.Enfermedades")
                enfermedades = cursor.fetchall()
                if enfermedades:
                    chat_display.insert(tk.END, "Bot: Estas son las enfermedades registradas:\n")
                    for enf in enfermedades:
                        chat_display.insert(tk.END, f"- {enf[0]}: {enf[1]}\n")
                else:
                    chat_display.insert(tk.END, "Bot: No hay información sobre enfermedades.\n")
            except Exception as ex:
                chat_display.insert(tk.END, f"Bot: Error al obtener información sobre enfermedades: {ex}\n")

        elif "plagas" in mensaje or mensaje == "4":
            try:
                cursor.execute("SELECT Plaga, Descripcion FROM dbo.Plagas")
                plagas = cursor.fetchall()
                if plagas:
                    chat_display.insert(tk.END, "Bot: Estas son las plagas registradas:\n")
                    for plaga in plagas:
                        chat_display.insert(tk.END, f"- {plaga[0]}: {plaga[1]}\n")
                else:
                    chat_display.insert(tk.END, "Bot: No hay información sobre plagas.\n")
            except Exception as ex:
                chat_display.insert(tk.END, f"Bot: Error al obtener información sobre plagas: {ex}\n")

        elif "compatibilidad de cultivos" in mensaje or mensaje == "5":
            try:
                cursor.execute("SELECT Cultivo, Descripcion FROM dbo.Compatibilidad_Cultivo")
                compatibilidad = cursor.fetchall()
                if compatibilidad:
                    chat_display.insert(tk.END, "Bot: Aquí tienes información sobre compatibilidad de cultivos:\n")
                    for cultivo in compatibilidad:
                        chat_display.insert(tk.END, f"- {cultivo[0]}: {cultivo[1]}\n")
                else:
                    chat_display.insert(tk.END, "Bot: No hay información de compatibilidad de cultivos.\n")
            except Exception as ex:
                chat_display.insert(tk.END, f"Bot: Error al obtener información: {ex}\n")

        elif "etapas del cultivo" in mensaje or mensaje == "6":
            try:
                # Consulta para obtener las etapas del cultivo con sus descripciones
                cursor.execute("SELECT Nombre_Etapa, Descripción FROM dbo.Tipo_Cultivo_Etapas")
                etapas = cursor.fetchall()
                if etapas:
                    chat_display.insert(tk.END, "Bot: Estas son todas las etapas del cultivo de papa:\n")
                    for etapa in etapas:
                        nombre_etapa = etapa[0]  # Columna 'Nombre_Etapa'
                        descripcion_etapa = etapa[1]  # Columna 'Descripcion'
                        chat_display.insert(tk.END, f"- {nombre_etapa}: {descripcion_etapa}\n")
                else:
                    chat_display.insert(tk.END, "Bot: No hay información disponible sobre las etapas del cultivo.\n")
            except Exception as ex:
                chat_display.insert(tk.END, f"Bot: Error al obtener información sobre las etapas: {ex}\n")

        else:
            chat_display.insert(tk.END, "Bot: Lo siento, no entendí tu pregunta. Por favor, selecciona una opción válida.\n")

        chat_display.insert(tk.END, "\nBot: ¿Te gustaría preguntar algo más? Escribe 'sí' para ver las opciones nuevamente o 'no' para salir.\n")
        chat_display.config(state="disabled")

    # Función para manejar el envío de mensajes
    def enviar_mensaje():
        mensaje = chat_entry.get()
        chat_entry.delete(0, tk.END)
        chat_display.config(state="normal")
        chat_display.insert(tk.END, f"Tú: {mensaje}\n")
        chat_display.config(state="disabled")

        if mensaje.lower() in ["sí", "si"]:
            mostrar_opciones()
        elif mensaje.lower() == "no":
            chat_display.config(state="normal")
            chat_display.insert(tk.END, "Bot: ¡Gracias por usar el chatbot! Hasta luego.\n")
            chat_display.config(state="disabled")
        else:
            procesar_mensaje(mensaje)

# Ejecutar aplicación
if __name__ == "__main__":
    connection, cursor = conectar_bd()
    app = tk.Tk()
    login(app)
    app.mainloop()
