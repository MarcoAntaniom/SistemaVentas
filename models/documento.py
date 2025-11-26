from config.conexion import ConexionDB

class Documentos:

    documento_id: int
    tipo_cliente_id: int
    tipo_documento: str

    def obtener_tipo_documento(self):
        try:
            c = ConexionDB()
            sql = "SELECT documento_id, tipo_documento FROM documento ORDER BY documento_id"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        
        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            if c:
                c.cursor.close()
                c.conexion.close()
