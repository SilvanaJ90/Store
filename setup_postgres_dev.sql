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
INSERT INTO myapp_product (id, name, description, price, available_units, image, brand, category_id) VALUES
(1, 'Aretes 1', 'Descripción para aretes 1', 10.00, 50, '/product_images/aretes/1.jpeg', 'Brand A', 1),
(2, 'Aretes 2', 'Descripción para aretes 2', 12.00, 60, '/product_images/aretes/2.jpeg', 'Brand B', 1),
(3, 'Aretes 3', 'Descripción para aretes 3', 4.00, 7, '/product_images/aretes/3.jpeg', 'Brand C', 1),
(4, 'Aretes 4', 'Descripción para aretes 4', 14.00, 0, '/product_images/aretes/4.jpeg', 'Brand C', 1),
(5, 'Aretes 5', 'Descripción para aretes 5', 7.00, 80, '/product_images/aretes/5.jpeg', 'Brand C', 1),
(6, 'Aretes 6', 'Descripción para aretes 6', 8.00, 90, '/product_images/aretes/6.jpeg', 'Brand C', 1),
(7, 'Aretes 7', 'Descripción para aretes 7', 5.00, 100, '/product_images/aretes/7.jpeg', 'Brand C', 1),
(8, 'Aretes 8', 'Descripción para aretes 8', 14.00, 70, '/product_images/aretes/8.jpeg', 'Brand C', 1),
(9, 'Aretes 9', 'Descripción para aretes 9', 15.00, 70, '/product_images/aretes/9.jpeg', 'Brand C', 1),
(10, 'Aretes 10', 'Descripción para aretes 10', 20.00, 10, '/product_images/aretes/10.jpeg', 'Brand C', 1),
(11, 'Aretes 11', 'Descripción para aretes 11', 30.00, 3, '/product_images/aretes/11.jpeg', 'Brand C', 1),
(12, 'Aretes 12', 'Descripción para aretes 12', 14.00, 8, '/product_images/aretes/12.jpeg', 'Brand C', 1),
(13, 'Aretes 13', 'Descripción para aretes 13', 14.00, 20, '/product_images/aretes/13.jpeg', 'Brand C', 1),
(14, 'Aretes 14', 'Descripción para aretes 14', 80.00, 30, '/product_images/aretes/14.jpeg', 'Brand C', 1),
(15, 'Aretes 15', 'Descripción para aretes 15', 10.00, 100, '/product_images/aretes/15.jpeg', 'Brand C', 1),
(16, 'Aretes 16', 'Descripción para aretes 16', 15.00, 50, '/product_images/aretes/16.jpeg', 'Brand C', 1),
(17, 'Aretes 17', 'Descripción para aretes 17', 15.00, 30, '/product_images/aretes/17.jpeg', 'Brand C', 1),
(18, 'Aretes 18', 'Descripción para aretes 18', 12.00, 20, '/product_images/aretes/18.jpeg', 'Brand C', 1),
(19, 'Aretes 19', 'Descripción para aretes 19', 14.00, 55, '/product_images/aretes/19.jpeg', 'Brand C', 1),
(20, 'Aretes 20', 'Descripción para aretes 20', 15.00, 70, '/product_images/aretes/20.jpeg', 'Brand C', 1),
(21, 'Aretes 21', 'Descripción para aretes 21', 20.00, 10, '/product_images/aretes/21.jpeg', 'Brand C', 1),
(22, 'Aretes 22', 'Descripción para aretes 22', 30.00, 3, '/product_images/aretes/22.jpeg', 'Brand C', 1),
(23, 'Aretes 23', 'Descripción para aretes 23', 14.00, 8, '/product_images/aretes/23.jpeg', 'Brand C', 1),
(24, 'Aretes 24', 'Descripción para aretes 24', 14.00, 20, '/product_images/aretes/24.jpeg', 'Brand C', 1),
(25, 'Aretes 25', 'Descripción para aretes 25', 80.00, 30, '/product_images/aretes/25.jpeg', 'Brand C', 1),
(26, 'Aretes 26', 'Descripción para aretes 26', 10.00, 100, '/product_images/aretes/26.jpeg', 'Brand C', 1),
(27, 'Aretes 27', 'Descripción para aretes 26', 15.00, 50, '/product_images/aretes/27.jpeg', 'Brand C', 1),
(28, 'Aretes 28', 'Descripción para aretes 28', 15.00, 30, '/product_images/aretes/28.jpeg', 'Brand C', 1),
(29, 'Aretes 29', 'Descripción para aretes 29', 12.00, 20, '/product_images/aretes/29.jpeg', 'Brand C', 1),
(30, 'Aretes 30', 'Descripción para aretes 30', 14.00, 55, '/product_images/aretes/30.jpeg', 'Brand C', 1),
(31, 'Aretes 31', 'Descripción para aretes 31', 14.00, 55, '/product_images/aretes/31.jpeg', 'Brand C', 1),
(32, 'Aretes 32', 'Descripción para aretes 32', 14.00, 55, '/product_images/aretes/32.jpeg', 'Brand C', 1),
(33, 'Aretes 33', 'Descripción para aretes 33', 14.00, 55, '/product_images/aretes/33.jpeg', 'Brand C', 1),
(34, 'Aretes 34', 'Descripción para aretes 34', 22.00, 80, '/product_images/aretes/34.jpeg', 'Brand Z', 1);

-- Insertar productos de collares
INSERT INTO myapp_product (id, name, description, price, available_units, image, brand, category_id) VALUES
(35, 'Collar 35', 'Descripción para collar 35', 15.00, 55, '/product_images/collares/35.jpeg', 'Brand X', 2),
(36, 'Collar 36', 'Descripción para collar 36', 18.00, 65, '/product_images/collares/36.jpeg', 'Brand Y', 2),
(37, 'Collar 37', 'Descripción para collar 37', 20.00, 75, '/product_images/collares/37.jpeg', 'Brand Z', 2),
(38, 'Collar 38', 'Descripción para collar 38', 15.00, 55, '/product_images/collares/38.jpeg', 'Brand X', 2),
(39, 'Collar 39', 'Descripción para collar 39', 18.00, 65, '/product_images/collares/39.jpeg', 'Brand Y', 2),
(40, 'Collar 40', 'Descripción para collar 40', 20.00, 75, '/product_images/collares/40.jpeg', 'Brand Z', 2),
(41, 'Collar 41', 'Descripción para collar 41', 15.00, 55, '/product_images/collares/41.jpeg', 'Brand X', 2),
(42, 'Collar 42', 'Descripción para collar 42', 18.00, 65, '/product_images/collares/42.jpeg', 'Brand Y', 2),
(43, 'Collar 43', 'Descripción para collar 43', 20.00, 75, '/product_images/collares/43.jpeg', 'Brand Z', 2),
(44, 'Collar 44', 'Descripción para collar 44', 15.00, 55, '/product_images/collares/44.jpeg', 'Brand X', 2),
(45, 'Collar 45', 'Descripción para collar 45', 18.00, 65, '/product_images/collares/45.jpeg', 'Brand Y', 2),
(46, 'Collar 46', 'Descripción para collar 46', 20.00, 75, '/product_images/collares/46.jpeg', 'Brand Z', 2),
(47, 'Collar 47', 'Descripción para collar 47', 15.00, 55, '/product_images/collares/47.jpeg', 'Brand X', 2),
(48, 'Collar 48', 'Descripción para collar 48', 18.00, 65, '/product_images/collares/48.jpeg', 'Brand Y', 2),
(49, 'Collar 49', 'Descripción para collar 49', 20.00, 75, '/product_images/collares/49.jpeg', 'Brand Z', 2),
(50, 'Collar 50', 'Descripción para collar 50', 20.00, 75, '/product_images/collares/49.jpeg', 'Brand Z', 2),
(51, 'Collar 51', 'Descripción para collar 51', 20.00, 75, '/product_images/collares/50.jpeg', 'Brand Z', 2),
(52, 'Collar 52', 'Descripción para collar 52', 20.00, 75, '/product_images/collares/51.jpeg', 'Brand Z', 2),
(53, 'Collar 53', 'Descripción para collar 53', 20.00, 75, '/product_images/collares/52.jpeg', 'Brand Z', 2),
(54, 'Collar 54', 'Descripción para collar 54', 25.00, 85, '/product_images/collares/53.jpeg', 'Brand W', 2);
