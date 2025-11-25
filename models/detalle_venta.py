from config.conexion import ConexionDB

class Detalle_venta: 

    folio_id: int 
    producto_id: int
    cantidad: int
    subtotal: int

    def insertar_detalle(self):
        try:
            c = ConexionDB()
            sql = """INSERT INTO detalle_venta (folio_id, producto_id, cantidad, subtotal)
                        VALUES (:folio, :producto, :cant, :subtotal)"""
            c.cursor.execute(sql, folio=self.folio_id, producto=self.producto_id, cant=self.cantidad, subtotal=self.subtotal)
            c.conexion.commit()

        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            if c:
                c.cursor.close()
                c.conexion.close()

