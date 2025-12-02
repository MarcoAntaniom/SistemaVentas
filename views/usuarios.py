import tkinter as tk
from tkinter import ttk, messagebox
from models.usuarios import Usuario

class Vista_usuarios(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        self.vista_usuarios()

    def vista_usuarios(self):
        pass