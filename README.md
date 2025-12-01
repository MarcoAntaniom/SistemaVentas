# SistemaVentas
Proyecto de Funciones y Matrices 

### 21 De Noviembre 2025
#### Marco Milanca
- Se crea la Conexión con la Base de Datos.
- Se arreglan errores en el script SQL.

### 22 De Noviembre 2025
#### Marco Milanca
- Se agrega un .gitignore para ignorar todas las carpetas del caché de Python.
- Se deja funcionando parcialmente el método ingresar_venta.
- Se crea y deja funcionando el insertar_detalle.

### 24 De Noviembre 2025
#### Marco Milanca
- Se integra Tkinter para la interfaz gráfica del sistema.
- Se deja parcialmente funcionando el apartado de ingresar_venta con interfaz gráfica. 
- Se agrega el método actualizar_total que actualiza el monto total de una venta al terminarla.
- Se agrega un método que llama a los productos que hay en la Base de Datos.

### 25 De Noviembre 2025
#### Marco Milanca
- Se deja Funcinando parcialmente el insertar_detalle en la interfaz.
- Se agrega una nueva tabla, al insertar un producto en la Base de Datos se ve en la tabla detalle.
- Se agrega una imagen(temporal)
- al momento de hacer la venta y insertar productos en el detalle, se actualiza el total de la venta, tanto en la interfaz como en la Base de Datos.

### 26 De Noviembre 2025
#### Marco Milanca
- Se modifica el flujo de venta, ahora al presionar el btn ingresar venta se guarda en la Base de datos el detalle y se actualiza la cantidad del producto.
- Se cambio la img que era temporal.
- Se agrego un select para seleccionar un tipo de documento (Boleta o Factura).
- Se borro el metodo actualizar_total, ahora es parte de ingresar_venta.
- Se crea un archivo que crea la Boleta/Factura en pdf, utilizando la libreria reportlab, este mismo se genera y se abre automáticamente al ingresar la venta en la Base de Datos.
- Las Boletas/Facturas se guardan en una carpeta por ordenadas por año y mes.

### 28 De Noviembre 2025
#### Juaquin Álvarez
- Se crea el modulo usuarios con el apartado de crear un nuevo usuario y uno mas usuarios.
- Se deja en funcionamiento temporal crear usuario para el testeo del modulo.

### 29 De Noviembre 2025
#### Marco Milanca
- Se agrega la documentación.
- Se crea el login, y se deja funcionando correctamente.
- Se modifica el app para manejar redireccionamiento con rol_id.
- En ingresar_venta el rut ya se obtiene automáticamente desde el inicio de sesión, y el input se bloqueo para que no pueda ser cambiado.
- se crea el archivo requirements.txt para instalar automáticamente las librerias que se utilizan.
- Para instalar las librerias con requirements.txt hay que hacer lo siguiente en la terminal: `pip install -r requirements.txt`
- Se modifica el documento para que se vea mas profesional, y se incluye el logo de MiniYa!.

### 30 De Noviembre 2025
#### Juaquin Álvarez
- Se termina de codificar el apartado de la creación de nuevos usuarios para que funcione correctamente, al igual que la encriptación de sus claves, la búsqueda de todos los usuarios existentes y la búsqueda de un solo usuario a través de su RUT.

### 1 De Noviembre 2025
#### Juaquin Álvarez
- Se agrego la función de buscar todas las ventas dejandola funcional.
-se crearon las clases de proveedor y compra para la incorporacion de nuevas funciones.
-se agrego la funcion de agregar compra dejandola funcional para la interfaz
-se agrego la funcion de actualizar proveedor dejandola funcional para la interfaz y cambiar cierta informacion de ellos.
