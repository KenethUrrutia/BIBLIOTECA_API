-- Active: 1718984771243@@localhost@5053@BIBLIOTECADBTEST
-- MySQL Script generated by MySQL Workbench

-- -----------------------------------------------------
-- Schema BIBLIOTECADBTEST
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BIBLIOTECADBTEST
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `BIBLIOTECADBTEST`;

CREATE SCHEMA IF NOT EXISTS `BIBLIOTECADBTEST` DEFAULT CHARACTER SET utf8;

USE `BIBLIOTECADBTEST`;

-- -----------------------------------------------------
-- Table `BIBLIOTECADBTEST`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BIBLIOTECADBTEST`.`USUARIO` (
    `IDUSUARIO` INT NOT NULL AUTO_INCREMENT,
    `NOMBRE` VARCHAR(200) NOT NULL,
    `APELLIDO` VARCHAR(200) NULL,
    `EDAD` TINYINT(2) NOT NULL,
    `CORREO` VARCHAR(45) NOT NULL,
    `PASSWORD` VARCHAR(20) NOT NULL,
    PRIMARY KEY (`IDUSUARIO`)
);

-- -----------------------------------------------------
-- Table `BIBLIOTECADBTEST`.`GENERO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BIBLIOTECADBTEST`.`GENERO` (
    `IDGENERO` INT NOT NULL AUTO_INCREMENT,
    `NOMBRE` VARCHAR(10) NOT NULL,
    PRIMARY KEY (`IDGENERO`)
);

-- -----------------------------------------------------
-- Table `BIBLIOTECADBTEST`.`LIBRO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BIBLIOTECADBTEST`.`LIBRO` (
    `IDLIBRO` INT NOT NULL AUTO_INCREMENT,
    `TITULO` VARCHAR(200) NOT NULL,
    `AUTOR` VARCHAR(100) NULL,
    `ANIO_PUBLICACION` DATE NULL,
    `IDGENERO` INT NOT NULL,
    PRIMARY KEY (`IDLIBRO`),
    CONSTRAINT `fk_LIBRO_GENERO` FOREIGN KEY (`IDGENERO`) REFERENCES `BIBLIOTECADBTEST`.`GENERO` (`IDGENERO`) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table `BIBLIOTECADBTEST`.`ESTADO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BIBLIOTECADBTEST`.`ESTADO` (
    `IDESTADO` INT NOT NULL AUTO_INCREMENT,
    `NOMBRE` VARCHAR(45) NULL,
    PRIMARY KEY (`IDESTADO`)
);

-- -----------------------------------------------------
-- Table `BIBLIOTECADBTEST`.`PRESTAMO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BIBLIOTECADBTEST`.`PRESTAMO` (
    `IDUSUARIO` INT NOT NULL,
    `IDLIBRO` INT NOT NULL,
    `IDPRESTAMO` INT NOT NULL AUTO_INCREMENT,
    `FECHA_PRESTAMO` DATETIME NOT NULL,
    `FECHA_DEVOLUCION` DATETIME NULL,
    `ESTADO` VARCHAR(45) NULL,
    `IDESTADO` INT NOT NULL,
    PRIMARY KEY (`IDPRESTAMO`),
    CONSTRAINT `fk_PRESTAMO_USUARIO1` FOREIGN KEY (`IDUSUARIO`) REFERENCES `BIBLIOTECADBTEST`.`USUARIO` (`IDUSUARIO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT `fk_PRESTAMO_LIBRO1` FOREIGN KEY (`IDLIBRO`) REFERENCES `BIBLIOTECADBTEST`.`LIBRO` (`IDLIBRO`) ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT `fk_PRESTAMO_ESTADO1` FOREIGN KEY (`IDESTADO`) REFERENCES `BIBLIOTECADBTEST`.`ESTADO` (`IDESTADO`) ON DELETE NO ACTION ON UPDATE NO ACTION
);

INSERT INTO
    `USUARIO` (
        `NOMBRE`,
        `APELLIDO`,
        `EDAD`,
        `CORREO`,
        `PASSWORD`
    )
VALUES (
        'Ramiro',
        'Perez',
        18,
        'ramiro@gmail.com',
        '201940854'
    );