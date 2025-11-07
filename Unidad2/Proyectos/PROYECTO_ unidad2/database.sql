

DROP DATABASE IF EXISTS poo_proyect_p2;
CREATE DATABASE IF NOT EXISTS poo_proyect_p2;
USE poo_proyect_p2;


CREATE TABLE usuarios (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL DEFAULT 'usuario'
);

INSERT INTO usuarios (usuario, password, rol) VALUES ('administrador', '1234', 'administrador');



CREATE TABLE productos (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    stock INT NOT NULL DEFAULT 0
);


INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Gordita de Chicharrón', 'Gordita de chicharrón', 22.00, 100),
('Gordita de Carnitas', 'Gordita de carnitas', 25.00, 80),
('Refresco 600ml', 'Sodas varias (600ml)', 18.00, 200),
('Agua de Horchata 1L', 'Agua fresca (1L)', 35.00, 50),
('Taco de Carnitas', 'Taco de carnitas', 15.00, 150);