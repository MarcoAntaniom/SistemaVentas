CREATE TABLE rol (
    rol_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_rol VARCHAR2(30) NOT NULL,
    descripcion VARCHAR2(100)
);

CREATE TABLE estado_usuario (
    estado_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(30) NOT NULL
);

CREATE TABLE usuario (
    RUT VARCHAR2(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR2(30) NOT NULL,
    apellido_paterno VARCHAR2(30) NOT NULL,
    apellido_materno VARCHAR2(30) NOT NULL,
    estado_id NUMBER NOT NULL,
    contrasena VARCHAR2(100) NOT NULL,
    rol_id NUMBER NOT NULL,
    CONSTRAINT fk_usuario_rol FOREIGN KEY (rol_id) REFERENCES rol(rol_id),
    CONSTRAINT fk_usuario_estado FOREIGN KEY (estado_id) REFERENCES estado_usuario(estado_id)
);

CREATE TABLE estado_producto (
    estado_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(30) NOT NULL
);

CREATE TABLE estado_venta (
    estado_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(30) NOT NULL
);

CREATE TABLE tipo_producto (
    tipo_producto_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(60) NOT NULL
);

CREATE TABLE productos (
    producto_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(50) NOT NULL,
    cantidad NUMBER NOT NULL,
    tipo_producto_id NUMBER NOT NULL,
    precio_unitario NUMBER(12,2) NOT NULL,
    estado_producto_id NUMBER NOT NULL,
    CONSTRAINT fk_tipo_producto FOREIGN KEY (tipo_producto_id) REFERENCES tipo_producto(tipo_producto_id),
    CONSTRAINT fk_producto_estado FOREIGN KEY (estado_producto_id) REFERENCES estado_producto(estado_id)
);

CREATE TABLE tipo_cliente (
    tipo_cliente_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(30) NOT NULL
);

CREATE TABLE documento (
    documento_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    tipo_cliente_id NUMBER NOT NULL,
    tipo_documento VARCHAR2(20) NOT NULL,
    CONSTRAINT fk_documento_tipocliente FOREIGN KEY (tipo_cliente_id) REFERENCES tipo_cliente(tipo_cliente_id)
);

CREATE TABLE ventas (
    folio NUMBER PRIMARY KEY NOT NULL,
    rut_vendedor VARCHAR2(10) NOT NULL,
    fecha_venta DATE NOT NULL,
    estado_venta_id NUMBER NOT NULL,
    documento_id NUMBER NOT NULL,
    total_venta NUMBER(12,2) NULL,
    CONSTRAINT fk_venta_estado FOREIGN KEY (estado_venta_id) REFERENCES estado_venta(estado_id),
    CONSTRAINT fk_venta_documento FOREIGN KEY (documento_id) REFERENCES documento(documento_id),
    CONSTRAINT fk_rut_vendedor FOREIGN KEY (rut_vendedor) REFERENCES usuario(RUT)
);

CREATE TABLE detalle_venta (
    detalle_venta_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    folio_id NUMBER NOT NULL,
    producto_id NUMBER NOT NULL,
    cantidad NUMBER NOT NULL,
    subtotal NUMBER(12,2) NOT NULL,
    CONSTRAINT fk_detalleventa_folio FOREIGN KEY (folio_id) REFERENCES ventas(folio),
    CONSTRAINT fk_detalleventa_producto FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

CREATE TABLE proveedores (
    proveedor_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    nombre VARCHAR2(50) NOT NULL,
    RUT VARCHAR2(10) NOT NULL,
    contacto VARCHAR2(15) NOT NULL
);

CREATE TABLE compra (
    folio NUMBER PRIMARY KEY NOT NULL,
    proveedor_id NUMBER NOT NULL,
    fecha_compra DATE NOT NULL,
    total NUMBER(12,2) NULL,
    CONSTRAINT fk_compra_proveedor FOREIGN KEY (proveedor_id) REFERENCES proveedores(proveedor_id)
);

CREATE TABLE detalle_compra (
    detalle_compra_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL,
    folio_id NUMBER NOT NULL,
    producto_id NUMBER NOT NULL,
    cantidad NUMBER NOT NULL,
    subtotal NUMBER(12,2) NOT NULL,
    CONSTRAINT fk_detallecompra_folio FOREIGN KEY (folio_id) REFERENCES compra(folio),
    CONSTRAINT fk_detallecompra_producto FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

CREATE INDEX idx_detalleventa_producto ON detalle_venta(producto_id);
CREATE INDEX idx_detallecompra_producto ON detalle_compra(producto_id);
CREATE INDEX idx_ventas_estado ON ventas(estado_venta_id);
CREATE INDEX idx_productos_estado ON productos(estado_producto_id);