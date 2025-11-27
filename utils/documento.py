from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import datetime
import platform

# Este archivo se encarga de generar el pdf para la boleta o factura.

def generar_documento(folio, tipo_documento, productos, total):
    # Obtiene la fecha actual para sacar año y mes.
    ahora = datetime.datetime.now()
    anio = ahora.strftime("%Y")
    mes = ahora.strftime("%m")

    # Obtiene el directorio actual.
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Obtiene el directorio raíz.
    directorio_raiz = os.path.dirname(directorio_actual)

    # Ruta en la que se guardaran los archivos.
    ruta_carpeta = os.path.join(directorio_raiz, "documentos_emitidos", anio, mes)

    # Crea las carpetas si no existen
    os.makedirs(ruta_carpeta, exist_ok=True)

    nombre_archivo = f"{tipo_documento}_{folio}.pdf"
    ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

    c = canvas.Canvas(ruta_completa, pagesize=letter)
    width, height = letter

    # Lógica del pdf.
    titulo = "Comprobante de Venta"

    # Según el nombre del tipo_documento selecciona el nombre.
    if "Factura" in tipo_documento:
        titulo = "Factura Electrónica"
    
    elif "Boleta" in tipo_documento:
        titulo = "Boleta de Venta"
    
    # Encabezado.
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, titulo)

    c.setFont("Helvetica", 10)
    c.drawString(50, height - 100, f"Folio: {folio}")
    c.drawString(50, height - 115, f"Fecha: {datetime.date.today()}")
    
    # Detalle de Venta.
    y = height - 180
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Producto")
    c.drawString(250, y, "Precio")
    c.drawString(350, y, "Cant.")
    c.drawString(450, y, "Subtotal")

    y -= 20
    c.setFont("Helvetica", 10)

    # Obtiene los productos de la venta.
    for producto in productos:
        nombre = producto['nombre']
        precio = producto['precio_unitario']
        cantidad = producto['cantidad']
        subtotal = producto['subtotal']

        # Agrega los productos al pdf.
        c.drawString(50, y, f"{nombre}")
        c.drawString(250, y, f"{int(precio)}")
        c.drawString(350, y, f"{cantidad}")
        c.drawString(450, y, f"{int(subtotal)}")
        y -= 20

    # Total.
    c.setFont("Helvetica-Bold", 12)
    c.drawString(350, y - 20, "Total de la Venta:")
    c.drawString(450, y - 20, f"${int(total)}")

    # Finaliza y guarda.
    c.save()

    # Abre el archivo automáticamente
    try:
        if platform.system() == "Windows":
            os.startfile(ruta_completa)
        else:
            # Abre el archivo si esta en Linux/Mac
            import subprocess
            subprocess.call(["xdg-open", ruta_completa])
    except Exception as e:
        print(f"No se pudo abrir el archivo automáticamente: {e}")
