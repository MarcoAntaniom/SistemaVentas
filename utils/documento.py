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

    # Ruta al logo.
    ruta_logo = os.path.join(directorio_raiz, "img", "logo.png")

    try:
        c.drawImage(ruta_logo, 50, height - 100, width=80, height=80, preserveAspectRatio=True, mask="auto")
    except Exception as e:
        print(f"No se pudo cargar el logo: {e}")

    # Lógica del pdf.
    titulo = "Comprobante de Venta"

    # Según el nombre del tipo_documento selecciona el nombre.
    if "Factura" in tipo_documento:
        titulo = "Factura Electrónica"
    
    elif "Boleta" in tipo_documento:
        titulo = "Boleta de Venta"
    
    # Encabezado.
    c.setFont("Helvetica-Bold", 14)
    c.drawRightString(width - 50, height - 45, titulo)

    c.setFont("Helvetica", 10)
    c.drawRightString(width - 50, height - 75, f"Folio: {folio}")
    c.drawRightString(width - 50, height - 95, f"Fecha: {datetime.date.today()}")

    # Dibuja una línea.
    c.line(50, height - 110, width - 50, height - 110)
    
    # Detalle de Venta.
    y = height - 130
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Producto")
    c.drawString(250, y, "Precio")
    c.drawString(350, y, "Cant.")
    c.drawString(450, y, "Subtotal")

    y -= 25
    c.setFont("Helvetica", 10)

    # Obtiene los productos de la venta.
    for producto in productos:
        nombre = producto['nombre']
        precio = producto['precio_unitario']
        cantidad = producto['cantidad']
        subtotal = producto['subtotal']

        # Agrega los productos al pdf.
        c.drawString(50, y, f"{nombre}")
        c.drawString(250, y, f"${int(precio)}")
        c.drawString(350, y, f"{cantidad}")
        c.drawString(450, y, f"${int(subtotal)}")
        y -= 20

    # Dibuja una línea.
    c.line(350, y + 10, 500, y + 10)

    # Total.
    if "Factura" in tipo_documento:
        neto = int(total / 1.19)
        iva = int(total - neto)

        c.setFont("Helvetica", 10)

        # Muestra el neto.
        c.drawString(350, y - 20, "Monto Neto:")
        c.drawString(450, y - 20, f"${neto}")

        # Muestra el IVA.
        c.drawString(350, y - 35, "IVA (19%):")
        c.drawString(450, y - 35, f"${iva}")

        # Muestra el total.
        c.setFont("Helvetica-Bold", 12)
        c.drawString(350, y - 55, "Total a Pagar:")
        c.drawString(450, y - 55, f"${int(total)}")
        
    else:
        # Si es boleta, se muestra sin el desglose.
        c.setFont("Helvetica-Bold", 12)
        c.drawString(350, y - 20, "Total a Pagar:")
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
