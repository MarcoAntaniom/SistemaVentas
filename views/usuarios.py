import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from models.usuarios import Usuario


class Vista_usuarios(tb.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)
        self.pack(fill="both", expand=True)

        self.crear_interfaz()
        self.cargar_usuarios()

    # ------------------------- INTERFAZ -------------------------
    def crear_interfaz(self):

        titulo = tb.Label(
            self,
            text="Gestión de Usuarios",
            font=("Segoe UI", 20, "bold"),
            bootstyle=PRIMARY
        )
        titulo.pack(pady=10)

        # FORM CARD
        card = tb.Labelframe(self, text="Datos del Usuario", padding=15, bootstyle=INFO)
        card.pack(fill="x", pady=10)

        self.var_rut = tb.StringVar()
        self.var_nombre = tb.StringVar()
        self.var_ap = tb.StringVar()
        self.var_am = tb.StringVar()
        self.var_rol = tb.IntVar()
        self.var_estado = tb.IntVar()
        self.var_contrasena = tb.StringVar()

        campos = [
            ("RUT", self.var_rut),
            ("Nombre", self.var_nombre),
            ("Apellido Paterno", self.var_ap),
            ("Apellido Materno", self.var_am),
            ("Contraseña (solo al agregar)", self.var_contrasena),
            ("Rol (1=Admin, 2=Vendedor, 3=Gerente)", self.var_rol),
            ("Estado (1=Activo, 0=Inactivo)", self.var_estado),
        ]

        grid = tb.Frame(card)
        grid.pack()

        for i, (texto, var) in enumerate(campos):
            tb.Label(grid, text=texto).grid(row=i, column=0, sticky="w", padx=5, pady=5)
            tb.Entry(grid, textvariable=var, width=35).grid(row=i, column=1, padx=5, pady=5)

        # BOTONES
        boton_frame = tb.Frame(self)
        boton_frame.pack(pady=10)

        tb.Button(boton_frame, text="Agregar Usuario", bootstyle=SUCCESS, width=18,
                  command=self.agregar_usuario).pack(side="left", padx=8)

        tb.Button(boton_frame, text="Actualizar Usuario", bootstyle=PRIMARY, width=18,
                  command=self.actualizar_usuario).pack(side="left", padx=8)

        tb.Button(boton_frame, text="Deshabilitar Usuario", bootstyle=DANGER, width=18,
                  command=self.deshabilitar_usuario).pack(side="left", padx=8)

        # TABLA SIN CONTRASEÑA
        self.tabla = tb.Treeview(
            self,
            columns=("rut", "nombre", "ap", "am", "estado", "rol"),
            show="headings",
            height=10,
            bootstyle=INFO
        )

        encabezados = ["RUT", "Nombre", "Apellido P.", "Apellido M.", "Estado", "Rol"]

        for col, h in zip(self.tabla["columns"], encabezados):
            self.tabla.heading(col, text=h)
            self.tabla.column(col, anchor="center", width=120)

        self.tabla.pack(fill="both", expand=True, pady=15)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_fila)

    # ------------------------- TABLA -------------------------
    def cargar_usuarios(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        u = Usuario()
        usuarios = u.consultar_usu()

        # user = (rut, nombre, ap, am, estado, contra, rol)
        for user in usuarios:
            self.tabla.insert(
                "",
                "end",
                values=(user[0], user[1], user[2], user[3], user[4], user[6])
            )

    def seleccionar_fila(self, event):
        sel = self.tabla.selection()
        if not sel:
            return

        datos = self.tabla.item(sel[0], "values")

        self.var_rut.set(datos[0])
        self.var_nombre.set(datos[1])
        self.var_ap.set(datos[2])
        self.var_am.set(datos[3])
        self.var_estado.set(datos[4])
        self.var_rol.set(datos[5])

    # ------------------------- FUNCIONES CRUD -------------------------
    def agregar_usuario(self):
        if not self.var_contrasena.get():
            messagebox.showerror("Error", "Debe ingresar una contraseña.")
            return

        u = Usuario()
        u.rut = self.var_rut.get()
        u.nombre = self.var_nombre.get()
        u.apellido_paterno = self.var_ap.get()
        u.apellido_materno = self.var_am.get()
        u.contrasena = self.var_contrasena.get()
        u.estado_id = self.var_estado.get()
        u.rol_id = self.var_rol.get()

        u.agregar_usuario()
        self.cargar_usuarios()
        messagebox.showinfo("OK", "Usuario agregado correctamente.")

    def actualizar_usuario(self):
        u = Usuario()
        u.rut = self.var_rut.get()
        u.nombre = self.var_nombre.get()
        u.apellido_paterno = self.var_ap.get()
        u.apellido_materno = self.var_am.get()
        u.estado_id = self.var_estado.get()
        u.rol_id = self.var_rol.get()

        u.actualizar_usuario()
        self.cargar_usuarios()
        messagebox.showinfo("OK", "Usuario actualizado correctamente.")

    def deshabilitar_usuario(self):
        rut = self.var_rut.get()

        if not rut:
            messagebox.showerror("Error", "Seleccione un usuario.")
            return

        u = Usuario()
        u.deshabilitar_usuario(rut)

        self.cargar_usuarios()
        messagebox.showinfo("OK", "Usuario deshabilitado correctamente.")
