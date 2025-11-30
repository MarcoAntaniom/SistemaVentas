import tkinter as tk
import os
from tkinter import ttk, messagebox, simpledialog
from models.ventas import Ventas
from models.productos import Productos
from models.documento import Documentos
from utils.documento import generar_documento

class Vista_ventas(tk.Frame):
    def __init__(self, parent, rut):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Obtiene el rut del vendedor, desde el momento que inicio sesión.
        self.rut_vendedor = rut

        # Inicializa la variable para almacenar el total de la venta.
        self.total_venta = 0
        self.carrito = [] # Lista que guarda los productos seleccionados para el detalle.
        # Llama a la ventana.
        self.ventana_vista()
    
    # Vista que muestra el formulario para ingresar una venta.
    def ventana_vista(self):
        # Título del panel
        tk.Label(self, text="Ingresar Venta", font=("Arial", 16, "bold")).pack(pady=20)

        # Contenedor principal (Contiene todo lo que hay en la pantalla).
        frame_principal = tk.Frame(self)
        frame_principal.pack(fill="both", expand=True, padx=20, pady=10)

        # Panel izquierdo (Formulario).
        panel_izquierdo = tk.Frame(frame_principal, width=300)
        panel_izquierdo.pack(side="left", fill="y", padx=(0, 20))

        # Panel derecho (Tablas).
        panel_derecho = tk.LabelFrame(frame_principal)
        panel_derecho.pack(side="right", fill="both", expand=True)

        # Contenido panel izquierdo.
        # Total de venta.
        self.label_total = tk.Label(panel_izquierdo, text="Total: $0", font=("Arial", 22, "bold"), fg="green")
        self.label_total.pack(side="bottom", pady=(20, 40))

        # Formulario de Venta.
        frame_formulario = tk.Frame(panel_izquierdo)
        frame_formulario.pack(side="bottom", fill="x")

        # Inputs organizados en el panel izquierdo.
        contenedor_input = tk.Frame(frame_formulario)
        contenedor_input.pack()

        tk.Label(contenedor_input, text="Folio:", font=("Arial", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=10)
        self.entrada_folio = tk.Entry(contenedor_input, width=15)
        self.entrada_folio.grid(row=0, column=1, sticky="w", padx=5, pady=10)

        tk.Label(contenedor_input, text="RUT Vendedor:", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=10)
        self.entrada_rut = tk.Entry(contenedor_input, width=15)
        self.entrada_rut.grid(row=1, column=1, sticky="w", padx=5, pady=10)

        self.entrada_rut.insert(0, self.rut_vendedor) # Rellena el campo con el RUT del usuario que inicio sesión.
        self.entrada_rut.config(state="readonly")

        tk.Label(contenedor_input, text="Tipo de Documento:", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=10)
        self.select_documento = ttk.Combobox(contenedor_input, state="readonly", width=12)
        self.select_documento.grid(row=2, column=1, sticky="w", padx=5, pady=10)

        self.ids_documento = {} # Guarda el ID y el nombre de los documentos.

        try:
            d = Documentos()
            tipos_doc = d.obtener_tipo_documento()

            nombre_doc = []
            for id_doc, nom_doc in tipos_doc:
                nombre_doc.append(nom_doc)
                self.ids_documento[nom_doc] = id_doc
            
            self.select_documento['values'] = nombre_doc

            # Selecciona el primero por defecto.
            if nombre_doc:
                self.select_documento.current(0)
        
        except Exception as e:
            print(f"Error cargando combobox: {e}")

        # Botón
        btn = tk.Button(frame_formulario, text="Registrar Venta", bg="green", fg="white", font=("Arial", 11, "bold"), cursor="hand2", command=self.guardar_venta)
        btn.pack(fill="x", pady=25)

        # Imagen
        try:
            # dirtectorio actual
            directorio_actual = os.path.dirname(os.path.abspath(__file__))

            # Retrocede una carpeta para llegar a la raíz del proyecto
            directorio_raiz = os.path.dirname(directorio_actual)

            ruta_imagen = os.path.join(directorio_raiz, "img", "cajero.png")

            self.img_ref = tk.PhotoImage(file=ruta_imagen)
            label_imagen = tk.Label(panel_izquierdo, image=self.img_ref)
            label_imagen.pack(side="top", expand=True)

        except Exception as e:
            print("Imagen no encontrada.")
            tk.Label(panel_izquierdo, text="Imagen no encontrada. Contacte con el Administrador", fg="gray").pack(side="top", expand=True)

        # Contenido panel derecho.
        # Tabla de productos.
        productos_frame = tk.LabelFrame(panel_derecho, text="Catálogo de Productos", font=("Arial", 10, "bold"))
        productos_frame.pack(side="top", fill="both",expand=True, pady=(0, 10))

        columnas = ("producto_id", "nombre", "tipo_producto_id", "precio_unitario" ,"cantidad") # Se generan los nombres de las columnas.
        self.tabla_productos = ttk.Treeview(productos_frame, columns=columnas, show="headings")

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

        # Agrega una barra de scroll.
        barra_scroll = ttk.Scrollbar(productos_frame, orient="vertical", command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscrollcommand=barra_scroll.set)

        barra_scroll.pack(side="right", fill="y")
        self.tabla_productos.pack(fill="both", expand=True, padx=20, pady=10)

        # Al hacer doble click izquierdo se llama a la siguiente función.
        self.tabla_productos.bind("<Double-1>", self.seleccionar_producto)

        # Tabla de detalle venta.
        detalle_frame = tk.LabelFrame(panel_derecho, text="Carrito de Compra", font=("Arial", 10, "bold"), fg="blue")
        detalle_frame.pack(side="bottom", fill="both", expand=True)

        columna_detalle = ("producto_id", "precio_unitario", "cantidad", "subtotal")
        self.tabla_detalle = ttk.Treeview(detalle_frame, columns=columna_detalle, show="headings", height=6)

        self.tabla_detalle.heading("producto_id", text="Nombre Producto")
        self.tabla_detalle.heading("precio_unitario", text="Precio c/u")
        self.tabla_detalle.heading("cantidad", text="Cant.")
        self.tabla_detalle.heading("subtotal", text="Subtotal")

        self.tabla_detalle.column("producto_id", width=180, anchor="w")
        self.tabla_detalle.column("precio_unitario", width=80, anchor="e")
        self.tabla_detalle.column("cantidad", width=60, anchor="center")
        self.tabla_detalle.column("subtotal", width=80, anchor="e")

        # Barra de scroll para detalle.
        scroll_detalle = ttk.Scrollbar(detalle_frame, orient="vertical", command=self.tabla_detalle.yview)
        self.tabla_detalle.configure(yscrollcommand=scroll_detalle.set)

        scroll_detalle.pack(side="right", fill="y")
        self.tabla_detalle.pack(side="left", fill="both", expand=True)

        # Carga los datos de la tabla de productos.
        self.cargar_datos()

    def guardar_venta(self):
        folio = self.entrada_folio.get()
        # Verifica que se ingrese un folio.
        if not folio:
            messagebox.showwarning("Falta Información", "Por favor ingresa el número de Folio.")
            return
        try:
            folio = int(folio)
        except ValueError:
            messagebox.showerror("Error", "El Folio debe ser un número.")
            return

        rut_vendedor = self.entrada_rut.get()

        # Verifica que se haya ingresado el RUT del vendedor.
        if not rut_vendedor:
            messagebox.showwarning("Falta Información", " Por favor ingresa el RUT del vendedor")
            return
        
        seleccion = self.select_documento.get()

        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un tipo de documento")
            return
        
        # Se valida que hayan ingresado productos al carrito.
        if not hasattr(self, 'carrito') or not self.carrito:
            messagebox.showwarning("Carrito Vacío", "No has agregado productos a la venta.")
            return
        
        # Traduce el texto al ID.
        id_doc_select = self.ids_documento[seleccion]

        try:
            v = Ventas()
            v.folio = folio
            v.rut_vendedor = rut_vendedor
            v.documento_id = id_doc_select
            v.total = self.total_venta
            v.ingresar_venta(self.carrito)

            # Envia los datos para generar el pdf.
            generar_documento(
                folio=folio,
                tipo_documento=seleccion,
                productos=self.carrito,
                total=self.total_venta
            )

            # Limpia la interfaz.
            self.total_venta = 0 # Limpia el total.
            self.carrito = [] # Limpia el carrito

            self.entrada_folio.delete(0, tk.END) # Limpia el campo de folio.
            self.entrada_rut.delete(0, tk.END) # Limpia el campo de rut.

            # Asigna el primer campo como predeterminado.
            if self.select_documento['values']:
                self.select_documento.current(0)
            
            self.label_total.config(text="Total: $0") # Muestra el total en la interfaz.
            
            # Borrar items del carrito visual.
            for item in self.tabla_detalle.get_children():
                self.tabla_detalle.delete(item)

            # Carga los datos nuevamente.
            self.cargar_datos()
                
            messagebox.showinfo("Éxito", "Venta guardada")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def cargar_datos(self):
        try:
            # Recarga la tabla.
            for item in self.tabla_productos.get_children():
                self.tabla_productos.delete(item)

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

        # Si se cerro la pantalla emergente sin colocar cantidad.
        # No hace nada.
        if cantidad is None:
            return
        
        cant = int(cantidad)
        if cant <= 0:
            messagebox.showwarning("Cantidad Inválida", "La cantidad debe ser mayor a 0.")
            return

        # Verifica que no se haya ingresado más de la cantidad disponible en la Base de Datos.
        if cant > stock_actual:
            messagebox.showwarning("Stock insuficiente.", f"Solo quedan {stock_actual} unidades.")
            return

        subtotal = precio_unitario * cantidad

        producto = {
            'producto_id': id_producto,
            'nombre': nombre,
            'precio_unitario': precio_unitario,
            'cantidad': cant,
            'subtotal': subtotal
        }
        self.carrito.append(producto)

        # Muestra el producto seleccionado en la tabla detalle.
        self.tabla_detalle.insert("", tk.END, values=(nombre, int(precio_unitario), cant, int(subtotal)))

        # Muestra el total actualizado en la interfaz.
        self.total_venta += subtotal
        self.label_total.config(text=f"Total: ${int(self.total_venta)}")