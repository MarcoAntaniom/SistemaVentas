import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from models.usuarios import Usuario

class Iniciar_sesion(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.parent = parent
        self.pack(fill="both", expand=True)

        self.ventana_login()

    def ventana_login(self):
        tk.Label(self, text="Iniciar Sesión", font=("Arial", 16, "bold"), bg="white").pack(pady=20)

        # Logo.
        try:
            # Directorio actual.
            directorio_actual = os.path.dirname(os.path.abspath(__file__))

            # Directorio raíz.
            directorio_raiz = os.path.dirname(directorio_actual)

            # Ruta al logo.
            ruta_imagen = os.path.join(directorio_raiz, "img", "logo.png")

            logo_pil = Image.open(ruta_imagen)

            nuevo_tamano = (300, 300)
            logo_redimensionado = logo_pil.resize(nuevo_tamano, Image.Resampling.LANCZOS)

            self.logo = ImageTk.PhotoImage(logo_redimensionado)
            label_imagen = tk.Label(self, image=self.logo, bg="white")
            label_imagen.pack(side="top", pady=10)

        except Exception as e:
            print(f"Error al cargar imagen: {e}")
            tk.Label(self, text="[Logo no encontrado]", fg="gray").pack(pady=20)

        tk.Label(self, text="RUT:", font=("Arial", 10), bg="white").pack(padx=10, pady=(15, 5))
        
        self.entrada_rut = tk.Entry(self, width=15)
        self.entrada_rut.pack(padx=5, pady=10)

        tk.Label(self, text="Contraseña:", font=("Arial", 10), bg="white").pack(padx=10, pady=(15, 5))

        self.entrada_contrasena = tk.Entry(self, width=15, show="*")
        self.entrada_contrasena.pack(padx=5, pady=10)

        tk.Button(self, text="Iniciar Sesión", bg="green", fg="white" ,font=("Arial", 11, "bold"), command=self.validar_acceso).pack()
    
    def validar_acceso(self):
        rut = self.entrada_rut.get()
        contrasena = self.entrada_contrasena.get()

        try:
            u = Usuario()
            contrasena = contrasena.encode("utf-8")
            dato_usuario = u.iniciar_sesion(rut=rut, contrasena=contrasena)

            if dato_usuario:
                rol_id = dato_usuario
                messagebox.showinfo(title="Iniciando Sesión", message="Inicio de Sesión exitoso.")
                self.parent.login_exitoso(rol_id, rut)
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        except Exception as e:
            print(f"Error: {e}")
