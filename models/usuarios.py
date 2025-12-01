import bcrypt
from config.conexion import ConexionDB

class Usuario:

    rut:str
    nombre:str
    apellido_paterno:str
    apellido_materno:str
    estado_id:int
    contrasena:str
    rol_id:int

    def __str__(self):
        f"RUT: {self.rut} - NOMBRE: {self.nombre} - APELLIDO_PATERNO: {self.apellido_paterno} - APELLIDO_MATERNO: {self.apellido_materno} - ROL_ID: {self.rol_id} - ESTADO_ID: {self.estado_id} "

    def agregar_usuario(self):
        try:
            c = ConexionDB()

            hashed = bcrypt.hashpw(self.contrasena.encode('utf-8'), bcrypt.gensalt())
            self.contrasena = hashed.decode('utf-8')

            sql = """
            INSERT INTO usuario (rut, nombre, apellido_paterno, apellido_materno, estado_id, contrasena, rol_id)
            VALUES (:rut, :nombre, :apellido_paterno, :apellido_materno, :estado_id, :contrasena, :rol_id)
            """

            c.cursor.execute(sql,
                             rut=self.rut,
                             nombre=self.nombre,
                             apellido_paterno=self.apellido_paterno,
                             apellido_materno=self.apellido_materno,
                             estado_id=self.estado_id,
                             contrasena=self.contrasena,
                             rol_id=self.rol_id)

            c.conexion.commit()

        except Exception as e:
            print(f"ERROR EN LA BASE DE DATOS {e}")

        finally:
            c.cursor.close()
            c.conexion.close()

    def consultar_usu(self):
        try:
            c = ConexionDB()
            sql = "SELECT * FROM usuario"
            c.cursor.execute(sql)
            resultados = c.cursor.fetchall()
            return resultados

        except Exception as e:
            print(f"ERROR EN CONSULTA: {e}")
            return []

        finally:
            c.cursor.close()
            c.conexion.close()

    def buscar_usuario_rut(self, rut):
        try:
            c = ConexionDB()
            sql = "SELECT * FROM usuario WHERE rut = :rut"

            c.cursor.execute(sql, rut=rut)
            resultado = c.cursor.fetchone()

            return resultado

        except Exception as e:
            print(f"ERROR EN CONSULTA: {e}")
            return None

    def iniciar_sesion(self, rut, contrasena: bytes):
        try:
            c = ConexionDB()
            sql = "SELECT contrasena, rol_id FROM usuario WHERE rut = :rut"
            c.cursor.execute(sql, rut=rut)
            fila = c.cursor.fetchone()

            if fila:
                contrasena_guardada = fila[0]
                rol_id = fila[1]

                if bcrypt.checkpw(contrasena, contrasena_guardada.encode('utf-8')):
                    return rol_id
            else:
                return False
            
        except Exception as e:
            print(f"Error en la BD: {e}")
        finally:
            if c:
                c.cursor.close()
                c.conexion.close()
