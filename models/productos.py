from config.conexion import ConexionDB

class Productos:
    
    producto_id: int
    nombre: str
    cantidad: int
    tipo_producto_id: int
    precio_unitario: int
    estado_producto_id: int

    def mostrar_productos(self):
        try:
            c = ConexionDB()
            sql = "SELECT producto_id, nombre, tipo_producto_id, precio_unitario, cantidad FROM productos"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            c.cursor.close()
            c.conexion.close()

