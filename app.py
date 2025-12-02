import tkinter as tk
from views.login import Iniciar_sesion
from views.ventas import Vista_ventas
from views.menu_admin import Vista_admin

class App(tk.Tk):
    def __init__(self):
        # Inicializa la clase padre.
        super().__init__()

        # Configuración de la ventana.
        self.title("Sistema Gestión de Ventas - MiniYa!")
        self.geometry("950x650")

        self.mostrar_login()

    # Limpia la ventana.
    def limpiar_ventana(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    # Muestra el login primero.
    def mostrar_login(self):
        self.limpiar_ventana()
        self.geometry("475x590")
        Iniciar_sesion(self)

    def login_exitoso(self, rol_id, rut):
        self.limpiar_ventana()
        self.geometry("950x650")

        # Lógica de roles.
        if rol_id == 1:
            Vista_admin(self)
        elif rol_id == 2:
            Vista_ventas(self, rut)
        elif rol_id == 3:
            pass
            #Vista_gerente()
        else:
            tk.Label(self, text="Rol sin interfaz asignada").pack()

    def cerrar_sesion(self):
        self.mostrar_login()
