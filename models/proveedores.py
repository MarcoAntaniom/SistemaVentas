from config.conexion import ConexionDB

class Proveedor:

    proveedor_id:int
    nombre:str
    rut:str
    contacto:str


    def actualizar_proveedor(self):
        try:
            c = ConexionDB()

            sql = """
            UPDATE proveedor
            SET nombre = :nombre,
                contacto = :contacto
            WHERE rut = :rut
            """

            c.cursor.execute(sql,
                            nombre=self.nombre,
                            rut=self.rut,
                            contacto=self.contacto)

            c.conexion.commit()
            return True

        except Exception as e:
            print(f"ERROR AL ACTUALIZAR PROVEEDOR: {e}")
            return False

        finally:
            c.cursor.close()
            c.conexion.close()