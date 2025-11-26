from config.conexion import ConexionDB
import datetime

class Ventas:

    folio: int
    rut_vendedor: str
    fecha_venta: str
    estado_venta: int
    documento_id: int
    total: int

    # EL PRECIO QUE ESTA EN LA BD ESTA CON IVA.

    def ingresar_venta(self, lista_productos):
        try:
            fecha = datetime.date.today() # Se obtiene la fecha de hoy.
            c = ConexionDB()
            sql_venta = """INSERT INTO ventas (folio, rut_vendedor, fecha_venta, estado_venta_id, documento_id, total_venta) 
                        VALUES (:folio, :rut, :fecha, 1, :documento, :total)"""

            c.cursor.execute(sql_venta, folio=self.folio, rut=self.rut_vendedor, documento=self.documento_id, fecha=fecha, total=self.total)

            # Se inserta el detalle junto con la venta para mejorar el flujo anterior.
            sql_detalle = """INSERT INTO detalle_venta (folio_id, producto_id, cantidad, subtotal)
                                VALUES (:folio, :producto, :cant, :subtotal)"""
            
            sql_update_stock = "UPDATE productos SET cantidad = cantidad - :cant WHERE producto_id = :id"
            
            for producto in lista_productos:
                c.cursor.execute(sql_detalle,
                                 folio=self.folio,
                                 producto=producto['producto_id'],
                                 cant=producto['cantidad'],
                                 subtotal=producto['subtotal'])
                
                c.cursor.execute(sql_update_stock,
                                 cant=producto['cantidad'],
                                 id=producto['producto_id'])

            c.conexion.commit()

        except Exception as e:
            print(f"Error en la BD: {e}")
            if c:
                c.conexion.rollback()
        finally:
             if c:
                c.cursor.close()
                c.conexion.close()
                
    def anular_venta(self, folio):
        try:
            c = ConexionDB()
            sql = "UPDATE ventas SET estado_venta_id = 21 WHERE folio = :folio"
            c.cursor.execute(sql, folio=folio)
            c.conexion.commit()

        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            if c:
                c.cursor.close()
                c.conexion.close()
                
