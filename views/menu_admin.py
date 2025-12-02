import tkinter as tk
from views.usuarios import Vista_usuarios

class Vista_admin(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="both", expand=True)
        
        # Configuración visual.
        self.bg_sidebar = "#2c3e50"
        self.fg_sidebar = "white"
        self.font_btn = ("Arial", 10)

        # Layout Principal.
        self.sidebar = tk.Frame(self, bg=self.bg_sidebar, width=200)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.content_area = tk.Frame(self, bg="#ecf0f1")
        self.content_area.pack(side="right", fill="both", expand=True)

        self.crear_menu()
        self.mostrar_bienvenida()

    def crear_menu(self):
        tk.Label(self.sidebar, text="Panel del Administrador", bg=self.bg_sidebar, fg="white", 
                 font=("Arial", 12, "bold")).pack(pady=30)

        # Botones de navegación que cargan las clases.
        self.btn_nav("Usuarios", lambda: self.cambiar_vista(Vista_usuarios))

        # Espaciador.
        tk.Frame(self.sidebar, bg=self.bg_sidebar).pack(expand=True)
        
        btn_salir = tk.Button(self.sidebar, text="Cerrar Sesión", bg="#c0392b", fg="white",
                              font=self.font_btn, bd=0, pady=10, cursor="hand2",
                              command=self.parent.cerrar_sesion)
        btn_salir.pack(fill="x", side="bottom", pady=20, padx=10)

    def btn_nav(self, texto, comando):
        btn = tk.Button(self.sidebar, text=texto, bg=self.bg_sidebar, fg=self.fg_sidebar,
                        font=self.font_btn, bd=0, anchor="w", padx=20, pady=10,
                        activebackground="#34495e", activeforeground="white", cursor="hand2",
                        command=comando)
        btn.pack(fill="x")

    def cambiar_vista(self, clase_vista):
        # Limpia el área de contenido.
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        clase_vista(self.content_area)

    def mostrar_bienvenida(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

        tk.Label(self.content_area, text="Bienvenido al Panel de Control", 
                 font=("Arial", 24, "bold"), fg="#bdc3c7", bg="#ecf0f1").pack(expand=True)
        