import tkinter as tk
from views.ventas import Vista_ventas

class App(tk.Tk):
    def __init__(self):
        # Inicializa la clase padre.
        super().__init__()

        # Configuración de la ventana.
        self.title("Sistema Gestión de Ventas")
        self.geometry("800x600")

        self.vista_actual = Vista_ventas(self)



