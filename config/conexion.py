import oracledb

class ConexionDB:

    def __init__(self):
        user = "INACAP"
        password = "inacap"
        user = "SISTEMA_VENTAS"
        password = "ventas"
        dsn = "localhost/xe" # Cambiar en caso de que tengan localhost o otra IP.

        self.conexion = oracledb.connect(user=user, password=password, dsn=dsn)
        self.cursor = self.conexion.cursor()
