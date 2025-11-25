from config.conexion import ConexionDB
import datetime

class Ventas:

    folio: int
    rut_vendedor: str
    fecha_venta: str
    estado_venta: int
    documento_id: int
    total: int

    def ingresar_venta(self):
        try:
            total_inicial = 0
            fecha = datetime.date.today() # Se obtiene la fecha de hoy.
            c = ConexionDB()
            sql = """INSERT INTO ventas (folio, rut_vendedor, fecha_venta, estado_venta_id, documento_id, total_venta) 
                        VALUES (:folio, :rut, :fecha, 1, 1, :total)"""

            c.cursor.execute(sql, folio=self.folio, rut=self.rut_vendedor, fecha=fecha, total=total_inicial)
            c.conexion.commit()

        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
             if c:
                c.cursor.close()
                c.conexion.close()
    
    def actualizar_total(self, folio, total):
        try:
            c = ConexionDB()
            sql = "UPDATE ventas SET total_venta = :total WHERE folio = :folio"
            c.cursor.execute(sql, folio=folio, total=total)
            c.conexion.commit()

        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            if c:
                c.cursor.close()
                c.conexion.close()
                
