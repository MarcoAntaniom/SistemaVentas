import tkinter as tk
from tkinter import ttk, messagebox
from models.ventas import Ventas
from models.productos import Productos

class Vista_ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Llama a la ventana.
        self.ventana_vista()
    
    # Vista que muestra el formulario para ingresar una venta.
    def ventana_vista(self):
        # Título del panel
        tk.Label(self, text="Ingresar Venta", font=("Arial", 16, "bold")).pack(pady=20)

        # Campos del formulario.
        tk.Label(self, text="Folio:").pack()
        self.entrada_folio = tk.Entry(self)
        self.entrada_folio.pack(pady=5)

        tk.Label(self, text="RUT vendedor:").pack()
        self.entrada_rut = tk.Entry(self)
        self.entrada_rut.pack(pady=5)

        columnas = ("producto_id", "nombre", "tipo_producto_id") # Se generan los nombres de las columnas.
        self.tabla_productos = ttk.Treeview(self, columns=columnas, show="headings")

        # Define los encabezados.
        self.tabla_productos.heading("producto_id", text="ID")
        self.tabla_productos.heading("nombre", text="Nombre del producto")
        self.tabla_productos.heading("tipo_producto_id", text="Tipo de producto")

        self.tabla_productos.column("producto_id", width=80, anchor="center")
        self.tabla_productos.column("nombre", width=120, anchor="center")
        self.tabla_productos.column("tipo_producto_id", width=120, anchor="center")

        # Agrega una barra de scroll
        barra_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscrollcommand=barra_scroll.set)

        barra_scroll.pack(side="right", fill="y")
        self.tabla_productos.pack(fill="both", expand=True, padx=20, pady=10)

        self.cargar_datos()

        tk.Button(self, text="Registrar Venta", bg="green", fg="white", command=self.guardar_venta).pack(pady=20)

    def guardar_venta(self):
        folio = self.entrada_folio.get()
        rut_vendedor = self.entrada_rut.get()

        try:
            v = Ventas()
            v.folio = folio
            v.rut_vendedor = rut_vendedor
            v.ingresar_venta()
            messagebox.showinfo("Éxito", "Venta guardada")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def cargar_datos(self):
        try:
            p = Productos()
            datos = p.mostrar_productos()

            for producto in datos:
                self.tabla_productos.insert("", tk.END, values=producto)
        except Exception as e:
            print(f"Error al cargar vista: {e}")