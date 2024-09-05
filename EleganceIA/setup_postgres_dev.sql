-- create database --
CREATE DATABASE "elegance_db";
-- create role --
create role "elegance_dev" with password 'elegance_pwd';
-- Grant login permissions --
alter role "elegance_dev" with login;


-- grants roles -----
\c "elegance_db";
GRANT USAGE ON SCHEMA public TO "elegance_dev";
GRANT CREATE ON SCHEMA public TO "elegance_dev";
GRANT CONNECT ON DATABASE "elegance_db" TO "elegance_dev";
GRANT ALL PRIVILEGES ON DATABASE "elegance_db" TO "elegance_dev";

-- Insertar productos de aretes

-- Insertar categorías
INSERT INTO myapp_category (id, name, description, created_at, updated_at) VALUES
(1, 'Aretes', 'aretes de golfy, plata etc', NOW(), NOW()),
(2, 'Collares', 'collares de golfy, plata etc', NOW(), NOW());

-- Insertar productos para la categoría 'Aretes'
INSERT INTO myapp_product (id, name, description, price, available_units, image, brand, category_id, created_at, updated_at) VALUES
(1, 'Aretes 1', 'Descripción para aretes 1', 10.00, 50, '/product_images/aretes/1.jpeg', 'Brand A', 1, NOW(), NOW()),
(2, 'Aretes 2', 'Descripción para aretes 2', 12.00, 60, '/product_images/aretes/2.jpeg', 'Brand B', 1, NOW(), NOW()),
(3, 'Aretes 3', 'Descripción para aretes 3', 4.00, 7, '/product_images/aretes/3.jpeg', 'Brand C', 1, NOW(), NOW()),
(4, 'Aretes 4', 'Descripción para aretes 4', 14.00, 0, '/product_images/aretes/4.jpeg', 'Brand C', 1, NOW(), NOW()),
(5, 'Aretes 5', 'Descripción para aretes 5', 7.00, 80, '/product_images/aretes/5.jpeg', 'Brand C', 1, NOW(), NOW()),
(6, 'Aretes 6', 'Descripción para aretes 6', 8.00, 90, '/product_images/aretes/6.jpeg', 'Brand C', 1, NOW(), NOW()),
(7, 'Aretes 7', 'Descripción para aretes 7', 5.00, 100, '/product_images/aretes/7.jpeg', 'Brand C', 1, NOW(), NOW()),
(8, 'Aretes 8', 'Descripción para aretes 8', 14.00, 70, '/product_images/aretes/8.jpeg', 'Brand C', 1, NOW(), NOW()),
(9, 'Aretes 9', 'Descripción para aretes 9', 15.00, 70, '/product_images/aretes/9.jpeg', 'Brand C', 1, NOW(), NOW()),
(10, 'Aretes 10', 'Descripción para aretes 10', 20.00, 10, '/product_images/aretes/10.jpeg', 'Brand C', 1, NOW(), NOW()),
(11, 'Aretes 11', 'Descripción para aretes 11', 30.00, 3, '/product_images/aretes/11.jpeg', 'Brand C', 1, NOW(), NOW()),
(12, 'Aretes 12', 'Descripción para aretes 12', 14.00, 8, '/product_images/aretes/12.jpeg', 'Brand C', 1, NOW(), NOW()),
(13, 'Aretes 13', 'Descripción para aretes 13', 14.00, 20, '/product_images/aretes/13.jpeg', 'Brand C', 1, NOW(), NOW()),
(14, 'Aretes 14', 'Descripción para aretes 14', 80.00, 30, '/product_images/aretes/14.jpeg', 'Brand C', 1, NOW(), NOW()),
(15, 'Aretes 15', 'Descripción para aretes 15', 10.00, 100, '/product_images/aretes/15.jpeg', 'Brand C', 1, NOW(), NOW()),
(16, 'Aretes 16', 'Descripción para aretes 16', 15.00, 50, '/product_images/aretes/16.jpeg', 'Brand C', 1, NOW(), NOW()),
(17, 'Aretes 17', 'Descripción para aretes 17', 15.00, 30, '/product_images/aretes/17.jpeg', 'Brand C', 1, NOW(), NOW()),
(18, 'Aretes 18', 'Descripción para aretes 18', 12.00, 20, '/product_images/aretes/18.jpeg', 'Brand C', 1, NOW(), NOW()),
(19, 'Aretes 19', 'Descripción para aretes 19', 14.00, 55, '/product_images/aretes/19.jpeg', 'Brand C', 1, NOW(), NOW()),
(20, 'Aretes 20', 'Descripción para aretes 20', 15.00, 70, '/product_images/aretes/20.jpeg', 'Brand C', 1, NOW(), NOW()),
(21, 'Aretes 21', 'Descripción para aretes 21', 20.00, 10, '/product_images/aretes/21.jpeg', 'Brand C', 1, NOW(), NOW()),
(22, 'Aretes 22', 'Descripción para aretes 22', 30.00, 3, '/product_images/aretes/22.jpeg', 'Brand C', 1, NOW(), NOW()),
(23, 'Aretes 23', 'Descripción para aretes 23', 14.00, 8, '/product_images/aretes/23.jpeg', 'Brand C', 1, NOW(), NOW()),
(24, 'Aretes 24', 'Descripción para aretes 24', 14.00, 20, '/product_images/aretes/24.jpeg', 'Brand C', 1, NOW(), NOW()),
(25, 'Aretes 25', 'Descripción para aretes 25', 80.00, 30, '/product_images/aretes/25.jpeg', 'Brand C', 1, NOW(), NOW()),
(26, 'Aretes 26', 'Descripción para aretes 26', 10.00, 100, '/product_images/aretes/26.jpeg', 'Brand C', 1, NOW(), NOW()),
(27, 'Aretes 27', 'Descripción para aretes 27', 15.00, 50, '/product_images/aretes/27.jpeg', 'Brand C', 1, NOW(), NOW()),
(28, 'Aretes 28', 'Descripción para aretes 28', 15.00, 30, '/product_images/aretes/28.jpeg', 'Brand C', 1, NOW(), NOW()),
(29, 'Aretes 29', 'Descripción para aretes 29', 12.00, 20, '/product_images/aretes/29.jpeg', 'Brand C', 1, NOW(), NOW()),
(30, 'Aretes 30', 'Descripción para aretes 30', 14.00, 55, '/product_images/aretes/30.jpeg', 'Brand C', 1, NOW(), NOW()),
(31, 'Aretes 31', 'Descripción para aretes 31', 14.00, 55, '/product_images/aretes/31.jpeg', 'Brand C', 1, NOW(), NOW()),
(32, 'Aretes 32', 'Descripción para aretes 32', 14.00, 55, '/product_images/aretes/32.jpeg', 'Brand C', 1, NOW(), NOW()),
(33, 'Aretes 33', 'Descripción para aretes 33', 14.00, 55, '/product_images/aretes/33.jpeg', 'Brand C', 1, NOW(), NOW()),
(34, 'Aretes 34', 'Descripción para aretes 34', 22.00, 80, '/product_images/aretes/34.jpeg', 'Brand Z', 1, NOW(), NOW());

-- Insertar productos para la categoría 'Collares'
INSERT INTO myapp_product (id, name, description, price, available_units, image, brand, category_id, created_at, updated_at) VALUES
(35, 'Collar 35', 'Descripción para collar 35', 15.00, 55, '/product_images/collares/35.jpeg', 'Brand X', 2, NOW(), NOW()),
(36, 'Collar 36', 'Descripción para collar 36', 18.00, 65, '/product_images/collares/36.jpeg', 'Brand Y', 2, NOW(), NOW()),
(37, 'Collar 37', 'Descripción para collar 37', 20.00, 75, '/product_images/collares/37.jpeg', 'Brand Z', 2, NOW(), NOW()),
(38, 'Collar 38', 'Descripción para collar 38', 15.00, 55, '/product_images/collares/38.jpeg', 'Brand X', 2, NOW(), NOW()),
(39, 'Collar 39', 'Descripción para collar 39', 18.00, 65, '/product_images/collares/39.jpeg', 'Brand Y', 2, NOW(), NOW()),
(40, 'Collar 40', 'Descripción para collar 40', 20.00, 75, '/product_images/collares/40.jpeg', 'Brand Z', 2, NOW(), NOW()),
(41, 'Collar 41', 'Descripción para collar 41', 15.00, 55, '/product_images/collares/41.jpeg', 'Brand X', 2, NOW(), NOW());


-- Insert usuarios
INSERT INTO myapp_user (id, last_login, email, password, first_name, last_name, is_active, is_user, created_at, updated_at)
VALUES 
(1, NOW(), 'usuario10@example.com', 'password10', 'Paula', 'Ramírez', TRUE, TRUE, NOW(), NOW()),
(2, NOW(), 'usuario2@example.com', 'password2', 'María', 'Gómez', TRUE, TRUE, NOW(), NOW()),
(3, NOW(), 'usuario3@example.com', 'password3', 'Carlos', 'López', TRUE, TRUE, NOW(), NOW()),
(4, NOW(), 'usuario4@example.com', 'password4', 'Ana', 'Martínez', TRUE, TRUE, NOW(), NOW()),
(5, NOW(), 'usuario5@example.com', 'password5', 'Luis', 'Hernández', TRUE, TRUE, NOW(), NOW()),
(6, NOW(), 'usuario6@example.com', 'password6', 'Marta', 'Díaz', TRUE, TRUE, NOW(), NOW()),
(7, NOW(), 'usuario7@example.com', 'password7', 'Pedro', 'Sánchez', TRUE, TRUE, NOW(), NOW()),
(8, NOW(), 'usuario8@example.com', 'password8', 'Clara', 'Fernández', TRUE, TRUE, NOW(), NOW()),
(9, NOW(), 'usuario9@example.com', 'password9', 'Diego', 'Torres', TRUE, TRUE, NOW(), NOW()),
(10, NOW(), 'admin1@example.com', 'admin123', 'admin', 'admin', TRUE, FALSE, NOW(), NOW());


-- comentarios producto 1
INSERT INTO myapp_comments (id, content, created_at, product_id, user_id) VALUES
(1, 'Este producto es increíble, lo recomiendo mucho!', NOW(), 1, 1),
(2, 'Me encanta este producto, superó mis expectativas.', NOW(), 1, 2),
(3, 'Un producto excelente, lo volvería a comprar.', NOW(), 1, 3),
(4, 'Muy buen producto, estoy muy satisfecho.', NOW(), 1, 4),
(5, 'Recomiendo este producto a todos, es maravilloso.', NOW(), 1, 5),
(6, 'Producto de alta calidad, muy recomendable.', NOW(), 1, 6),
(7, 'Me ha gustado mucho, es justo lo que buscaba.', NOW(), 1, 1),
(8, 'Excelente compra, el producto es increíble.', NOW(), 1, 2),
(9, 'Muy bueno, cumple con lo prometido.', NOW(), 1, 3),
(10, 'Estoy muy feliz con mi compra, es fantástico.', NOW(), 1, 4),
(11, 'El producto es excelente, muy recomendado.', NOW(), 1, 5),
(12, 'Me ha impresionado, es mucho mejor de lo que esperaba.', NOW(), 1, 6),
(13, 'Producto de calidad superior, muy satisfecho.', NOW(), 1, 1),
(14, 'Totalmente recomendado, vale cada centavo.', NOW(), 1, 2),
(15, 'Excelente producto, no tengo ninguna queja.', NOW(), 1, 3),
(16, 'Muy buen producto, ha cumplido todas mis expectativas.', NOW(), 1, 4),
(17, 'Estoy muy contento con mi compra, es genial.', NOW(), 1, 5),
(18, 'El producto es increíble, superó mis expectativas.', NOW(), 1, 6),
(19, 'Un excelente producto, lo recomiendo sin dudarlo.', NOW(), 1, 1),
(20, 'Me ha sorprendido gratamente, muy buen producto.', NOW(), 1, 2),
(21, 'Muy satisfecho con el producto, lo volvería a comprar.', NOW(), 1, 3),
(22, 'El mejor producto que he comprado en mucho tiempo.', NOW(), 1, 4),
(23, 'Superó mis expectativas, es un producto excelente.', NOW(), 1, 5),
(24, 'Recomiendo este producto a todos, es muy bueno.', NOW(), 1, 6),
(25, 'Producto excelente, lo recomiendo ampliamente.', NOW(), 1, 1),
(26, 'Muy contento con la compra, el producto es genial.', NOW(), 1, 2),
(27, 'Un producto de gran calidad, estoy muy satisfecho.', NOW(), 1, 3),
(28, 'Es exactamente lo que necesitaba, muy recomendable.', NOW(), 1, 4),
(29, 'Estoy encantado con el producto, es excelente.', NOW(), 1, 5),
(30, 'Me ha gustado mucho, superó mis expectativas.', NOW(), 1, 6),
(31, 'Muy buen producto, lo recomendaría a cualquier persona.', NOW(), 1, 1),
(32, 'Producto de calidad, estoy muy contento con mi compra.', NOW(), 1, 2),
(33, 'Excelente, lo compraría de nuevo sin dudarlo.', NOW(), 1, 3),
(34, 'Producto fantástico, muy recomendable.', NOW(), 1, 4),
(35, 'Estoy muy satisfecho con el producto, es genial.', NOW(), 1, 5),
(36, 'Superó todas mis expectativas, es un gran producto.', NOW(), 1, 6),
(37, 'Me encanta este producto, ha sido una excelente compra.', NOW(), 1, 1),
(38, 'Producto muy bueno, lo recomiendo a todos.', NOW(), 1, 2),
(39, 'Estoy muy feliz con mi compra, es un excelente producto.', NOW(), 1, 3),
(40, 'Muy buen producto, ha cumplido con lo prometido.', NOW(), 1, 4),
(41, 'Excelente calidad, lo volvería a comprar.', NOW(), 1, 5),
(42, 'Un producto excepcional, estoy muy satisfecho.', NOW(), 1, 6),
(43, 'Me ha impresionado, es un producto increíble.', NOW(), 1, 1),
(44, 'Producto de alta calidad, muy recomendable.', NOW(), 1, 2),
(45, 'Estoy encantado con este producto, lo recomiendo.', NOW(), 1, 3),
(46, 'Producto excelente, estoy muy feliz con la compra.', NOW(), 1, 4),
(47, 'Es justo lo que necesitaba, muy buen producto.', NOW(), 1, 5),
(48, 'Un gran producto, ha superado mis expectativas.', NOW(), 1, 6),
(49, 'Muy buen producto, vale la pena cada centavo.', NOW(), 1, 1),
(50, 'Estoy muy satisfecho, el producto es excelente.', NOW(), 1, 2);


INSERT INTO myapp_comments (id, content, created_at, product_id, user_id) VALUES
(51, 'No me gustó el producto, no cumple con lo esperado.', NOW(), 2, 1),
(52, 'Muy decepcionado con la calidad del producto.', NOW(), 2, 2),
(53, 'El producto llegó defectuoso, no lo recomiendo.', NOW(), 2, 3),
(54, 'No es lo que prometen, muy insatisfecho.', NOW(), 2, 4),
(55, 'El producto no tiene buena relación calidad-precio.', NOW(), 2, 5),
(56, 'No cumple con las expectativas, estoy muy desilusionado.', NOW(), 2, 6),
(57, 'Producto de mala calidad, no lo compraría de nuevo.', NOW(), 2, 1),
(58, 'El producto es defectuoso, muy mala experiencia.', NOW(), 2, 2),
(59, 'No me ha gustado en absoluto, muy insatisfecho.', NOW(), 2, 3),
(60, 'El producto llegó tarde y en mal estado.', NOW(), 2, 4),
(61, 'No cumple con lo prometido, pésima compra.', NOW(), 2, 5),
(62, 'El producto es muy malo, no lo recomendaría.', NOW(), 2, 6),
(63, 'Desilusionado con la compra, esperaba más calidad.', NOW(), 2, 1),
(64, 'No lo compren, el producto es de mala calidad.', NOW(), 2, 2),
(65, 'El producto llegó con problemas, no lo recomiendo.', NOW(), 2, 3),
(66, 'No estoy satisfecho con el producto, es muy malo.', NOW(), 2, 4),
(67, 'El producto no es bueno, no vale la pena.', NOW(), 2, 5),
(68, 'No me gustó para nada, fue una mala compra.', NOW(), 2, 6),
(69, 'El producto llegó dañado, muy mala experiencia.', NOW(), 2, 1),
(70, 'No cumple con las expectativas, muy decepcionado.', NOW(), 2, 2),
(71, 'El producto es de mala calidad, no lo recomendaría.', NOW(), 2, 3),
(72, 'Muy insatisfecho con el producto, no lo volvería a comprar.', NOW(), 2, 4),
(73, 'No es lo que esperaba, producto muy deficiente.', NOW(), 2, 5),
(74, 'El producto no es bueno, lo devolvería si pudiera.', NOW(), 2, 6),
(75, 'Muy mala compra, el producto es de baja calidad.', NOW(), 2, 1),
(76, 'Descontento con el producto, no lo recomendaría a nadie.', NOW(), 2, 2),
(77, 'El producto es muy malo, no cumple con lo prometido.', NOW(), 2, 3),
(78, 'El producto llegó roto, no lo volvería a comprar.', NOW(), 2, 4),
(79, 'No es lo que esperé, muy mala calidad.', NOW(), 2, 5),
(80, 'No satisfecho con la compra, el producto es deficiente.', NOW(), 2, 6),
(81, 'El producto no tiene buena calidad, no lo recomiendo.', NOW(), 2, 1),
(82, 'La compra fue un error, el producto es muy malo.', NOW(), 2, 2),
(83, 'El producto llegó en mal estado, muy decepcionado.', NOW(), 2, 3),
(84, 'No cumple con lo que prometen, es de baja calidad.', NOW(), 2, 4),
(85, 'Muy desilusionado con el producto, no vale la pena.', NOW(), 2, 5),
(86, 'El producto no es lo que esperaba, muy insatisfecho.', NOW(), 2, 6),
(87, 'No lo compren, el producto es una decepción.', NOW(), 2, 1),
(88, 'El producto es muy malo, no lo volvería a comprar.', NOW(), 2, 2),
(89, 'No me gustó para nada, el producto es deficiente.', NOW(), 2, 3),
(90, 'La calidad del producto es muy baja, no lo recomiendo.', NOW(), 2, 4),
(91, 'Desilusionado con la compra, el producto es muy malo.', NOW(), 2, 5),
(92, 'El producto llegó en malas condiciones, no lo compraría de nuevo.', NOW(), 2, 6),
(93, 'No me ha gustado en absoluto, muy mala compra.', NOW(), 2, 1),
(94, 'El producto es defectuoso, no cumple con lo prometido.', NOW(), 2, 2),
(95, 'El producto no vale la pena, muy mala calidad.', NOW(), 2, 3),
(96, 'No estoy satisfecho con el producto, esperaba algo mejor.', NOW(), 2, 4),
(97, 'Producto muy deficiente, no lo recomendaría a nadie.', NOW(), 2, 5),
(98, 'El producto es una decepción, no lo volvería a comprar.', NOW(), 2, 6),
(99, 'Muy mala experiencia, el producto llegó dañado.', NOW(), 2, 1),
(100, 'No cumple con las expectativas, muy decepcionado.', NOW(), 2, 2);


-- Comentarios Positivos
INSERT INTO myapp_comments (id, content, created_at, product_id, user_id) VALUES
(101, 'Este producto es increíble, lo recomiendo mucho!', NOW(), 3, 1),
(102, 'Excelente calidad y muy buen precio, estoy muy satisfecho.', NOW(), 3, 2),
(103, 'Me ha encantado, superó mis expectativas.', NOW(), 3, 3),
(104, 'Definitivamente lo volvería a comprar, gran producto.', NOW(), 3, 4),
(105, 'Muy contento con la compra, cumple perfectamente con lo prometido.', NOW(), 3, 5),
(106, 'Un producto excelente, lo recomiendo a todos.', NOW(), 3, 6),
(107, 'Superó mis expectativas, muy buen producto.', NOW(), 3, 1),
(108, 'Perfecto para lo que necesitaba, muy satisfecho.', NOW(), 3, 2),
(109, 'Calidad increíble, estoy muy feliz con mi compra.', NOW(), 3, 3),
(110, 'El mejor producto en esta categoría, lo recomendaré.', NOW(), 3, 4),
(111, 'Gran relación calidad-precio, estoy muy satisfecho.', NOW(), 3, 5),
(112, 'Muy buen producto, lo volvería a comprar sin dudar.', NOW(), 3, 6),
(113, 'Excelente, justo lo que buscaba.', NOW(), 3, 1),
(114, 'Me ha sorprendido gratamente, muy buen producto.', NOW(), 3, 2),
(115, 'Muy contento con mi compra, lo recomiendo.', NOW(), 3, 3),
(116, 'Un producto excepcional, muy satisfecho.', NOW(), 3, 4),
(117, 'Muy buen producto, cumpliendo con lo prometido.', NOW(), 3, 5),
(118, 'Recomendado al 100%, excelente compra.', NOW(), 3, 6),
(119, 'El producto es excelente, lo volvería a comprar.', NOW(), 3, 1),
(120, 'Estoy muy feliz con la compra, gran calidad.', NOW(), 3, 2),
(121, 'El producto es maravilloso, superó todas mis expectativas.', NOW(), 3, 3),
(122, 'Una excelente compra, lo recomiendo sin dudar.', NOW(), 3, 4),
(123, 'Estoy muy satisfecho, excelente calidad.', NOW(), 3, 5),
(124, 'Muy buen producto, totalmente recomendado.', NOW(), 3, 6);

-- Comentarios Negativos
INSERT INTO myapp_comments (id, content, created_at, product_id, user_id) VALUES
(125, 'No me gustó el producto, no cumple con lo esperado.', NOW(), 3, 1),
(126, 'La calidad no es tan buena como esperaba.', NOW(), 3, 2),
(127, 'El producto llegó con defectos, no lo recomiendo.', NOW(), 3, 3),
(128, 'No es lo que esperaba, bastante decepcionado.', NOW(), 3, 4),
(129, 'El producto tiene una calidad inferior a la prometida.', NOW(), 3, 5),
(130, 'No cumplió con mis expectativas, muy insatisfecho.', NOW(), 3, 6),
(131, 'El producto llegó dañado, muy mala experiencia.', NOW(), 3, 1),
(132, 'No es lo que prometen, estoy bastante desilusionado.', NOW(), 3, 2),
(133, 'El producto es de baja calidad, no lo volvería a comprar.', NOW(), 3, 3),
(134, 'No estoy satisfecho con la compra, muy decepcionado.', NOW(), 3, 4),
(135, 'El producto no cumplió con lo prometido, mala compra.', NOW(), 3, 5),
(136, 'No lo recomiendo, el producto tiene muchos defectos.', NOW(), 3, 6),
(137, 'El producto es muy malo, no lo recomendaría a nadie.', NOW(), 3, 1),
(138, 'Desilusionado con el producto, no cumplió con mis expectativas.', NOW(), 3, 2),
(139, 'El producto no es lo que esperaba, bastante insatisfecho.', NOW(), 3, 3),
(140, 'Muy decepcionado con la compra, el producto es deficiente.', NOW(), 3, 4),
(141, 'La calidad es muy baja, no lo volvería a comprar.', NOW(), 3, 5),
(142, 'No cumplió con lo prometido, mala calidad.', NOW(), 3, 6);
