import oracledb

class ConexionDB:

    def __init__(self):
        user = "SISTEMA_VENTAS"
        password = "ventas"
        dsn = "192.168.1.20/xe" # Cambiar en caso de que tengan localhost o otra IP.

        self.conexion = oracledb.connect(user=user, password=password, dsn=dsn)
        self.cursor = self.conexion.cursor()
