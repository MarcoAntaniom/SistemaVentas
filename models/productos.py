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

    def deshabilitar_producto(self, producto_id):
        try:
            c = ConexionDB()
            sql = """
                UPDATE productos
                SET estado_producto_id = 2
                WHERE producto_id = :producto_id
            """

            c.cursor.execute(sql, producto_id=producto_id)
            c.conexion.commit()

            return True

        except Exception as e:
            print(f"Error al deshabilitar producto: {e}")
            return False

        finally:
            try:
                c.cursor.close()
                c.conexion.close()
            except:
                pass
