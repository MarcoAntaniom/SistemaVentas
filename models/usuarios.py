from config.conexion import ConexionDB

class Usuario:

    rut:str
    nombre:str
    apellido_paterno:str
    apellido_materno:str
    estado_id:int
    contrasena:str
    rol_id:int

    def agregar_usuario(self):
        try:
            c = ConexionDB()

            sql="INSERT INTO usuario VALUE(rut:,nombre:,apellido_paterno:,apellido_materno:,estado_id:,contrasena:,rol_id:)"

            c.conexion.execute(sql,rut=self.rut,nombre=self.nombre,apellido_paterno=self.apellido_paterno,apellido_materno=self.apellido_materno,estado_id=self.estado_id,contrasena=self.contrasena,rol_id=self.rol_id)
            c.conexion.commit()
        except Exception as e:
            print(f"ERROR EN LA BASE DE DATOS {e}")
    def consultar_usu(self):
        c = ConexionDB()
        sql="SELECT * FROM usuario;"
        c.conexion.execute(sql)
        c.conexion.commit()