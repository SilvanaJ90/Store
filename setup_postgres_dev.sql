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
