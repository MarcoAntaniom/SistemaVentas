from config.conexion import ConexionDB

class Detalle_venta: 

    folio_id: int 
    producto_id: int
    cantidad: int
    subtotal: int

    # Se elimina el insertar detalle de aquí para mejorar el flujo de venta.

        try:
            c = ConexionDB()

        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            if c:
                c.cursor.close()
                c.conexion.close()

