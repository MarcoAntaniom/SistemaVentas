from config.conexion import ConexionDB
import datetime

class Compra:

    folio: int
    proveedor_id: int
    fecha_compra: str
    total: int

    def ingresar_compra(self):
        try:
            fecha = datetime.date.today()
            c = ConexionDB()

            # 1. Insertar la compra
            sql_compra = """
                INSERT INTO compra (folio, proveedor_id, fecha_compra, total_compra)
                VALUES (:folio, :proveedor_id, :fecha, :total)
            """

            c.cursor.execute(sql_compra,
                             folio=self.folio,
                             proveedor_id=self.proveedor_id,
                             fecha=fecha,
                             total=self.total)

            c.conexion.commit()
            return True

        except Exception as e:
            print(f"ERROR AL INGRESAR COMPRA: {e}")
            if c:
                c.conexion.rollback()
            return False

        finally:
            if c:
                c.cursor.close()
                c.conexion.close()