CREATE DATABASE IF NOT EXISTS shortydb;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON shortydb.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
