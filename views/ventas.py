import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from models.ventas import Ventas
from models.detalle_venta import Detalle_venta
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

        columnas = ("producto_id", "nombre", "tipo_producto_id", "precio_unitario", "cantidad") # Se generan los nombres de las columnas.
        self.tabla_productos = ttk.Treeview(self, columns=columnas, show="headings")

        # Define los encabezados.
        self.tabla_productos.heading("producto_id", text="ID")
        self.tabla_productos.heading("nombre", text="Nombre del producto")
        self.tabla_productos.heading("tipo_producto_id", text="Tipo de producto")
        self.tabla_productos.heading("precio_unitario", text="Precio Unitario")
        self.tabla_productos.heading("cantidad", text="Cantidad Disponible")

        self.tabla_productos.column("producto_id", width=80, anchor="sw")
        self.tabla_productos.column("nombre", width=120, anchor="sw")
        self.tabla_productos.column("tipo_producto_id", width=120, anchor="sw")
        self.tabla_productos.column("precio_unitario", width=120, anchor="sw")
        self.tabla_productos.column("cantidad", width=120, anchor="sw")

        # Agrega una barra de scroll
        barra_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscrollcommand=barra_scroll.set)

        barra_scroll.pack(side="right", fill="y")
        self.tabla_productos.pack(fill="both", expand=True, padx=20, pady=10)

        # Al hacer doble click izquierdo se llama a la siguiente función.
        self.tabla_productos.bind("<Double-1>", self.seleccionar_producto)

        self.cargar_datos()

        tk.Button(self, text="Registrar Venta", bg="green", fg="white", command=self.guardar_venta).pack(pady=20)

    def guardar_venta(self):
        folio = self.entrada_folio.get()
        folio = int(folio)
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

    def seleccionar_producto(self, event):
        # Guarda el id del producto seleccionado.
        producto_id = self.tabla_productos.selection()

        # Verifica si se seleccionó un producto
        if not producto_id:
            return

        # Obtiene los valores.
        producto = self.tabla_productos.item(producto_id)
        valores = producto['values']

        # Se guardan los valores que llegan del producto_id
        id_producto = valores[0]
        nombre = valores[1]
        tipo_producto_id = valores[2]
        precio_unitario = float(valores[3])
        stock_actual = int(valores[4])

        # Guarda la cantidad que se va a insertar en la tabla detalle_venta
        cantidad = simpledialog.askinteger("Cantidad", f"Precio ${precio_unitario}\nStock: {stock_actual}\nIngresa la canitdad:")

        cant = int(cantidad)

        if cant:
            # Verifica que no se haya ingresado más de la cantidad disponible en la Base de Datos.
            if cant > stock_actual:
                messagebox.showwarning("Stock insuficiente.", f"Solo quedan {stock_actual} unidades.")
                return

            subtotal = precio_unitario * cantidad
            folio_id = self.entrada_folio.get()
            folio_id = int(folio_id)

            try:
                d = Detalle_venta()
                d.folio_id = folio_id
                d.producto_id = id_producto
                d.cantidad = cant
                d.subtotal = subtotal

                d.insertar_detalle()

            except Exception as e:
                messagebox.showerror("Error", str(e))