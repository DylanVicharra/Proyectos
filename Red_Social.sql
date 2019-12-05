SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

USE `mydb`;

CREATE  TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `idUsuario` INT(11) NOT NULL AUTO_INCREMENT ,
  `emailUsuario` VARCHAR(45) NOT NULL ,
  `passwordUsuario` VARCHAR(256) NOT NULL ,
  `nombreUsuario` VARCHAR(20) NOT NULL ,
  `apellidoUsuario` VARCHAR(20) NOT NULL ,
  `generoUsuario` VARCHAR(10) NOT NULL ,
  `fotoUsuario` MEDIUMBLOB NULL DEFAULT NULL ,
  PRIMARY KEY (`idUsuario`) ,
  UNIQUE INDEX `emailUsuario_UNIQUE` (`emailUsuario` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 10000
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE  TABLE IF NOT EXISTS `mydb`.`Publicacion` (
  `idPublicacion` INT(11) NOT NULL AUTO_INCREMENT ,
  `fechaPublicacion` DATETIME NOT NULL ,
  `textoPublicacion` TINYTEXT NOT NULL ,
  `imagenPublicacion` MEDIUMBLOB NULL DEFAULT NULL ,
  `Usuario_idUsuario` INT(11) NOT NULL ,
  PRIMARY KEY (`idPublicacion`) ,
  INDEX `fk_Publicacion_Usuario_idx` (`Usuario_idUsuario` ASC) ,
  CONSTRAINT `fk_Publicacion_Usuario`
    FOREIGN KEY (`Usuario_idUsuario` )
    REFERENCES `mydb`.`Usuario` (`idUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE  TABLE IF NOT EXISTS `mydb`.`Contacto` (
  `idContacto` INT(11) NOT NULL AUTO_INCREMENT ,
  `Usuario_idUsuario` INT(11) NOT NULL ,
  `Usuario_idUsuario2` INT(11) NOT NULL ,
  `estadoContacto` TINYINT(1) NOT NULL ,
  `Rol_idRol` INT(11) NULL DEFAULT NULL ,
  PRIMARY KEY (`idContacto`) ,
  INDEX `fk_Contacto_Usuario1_idx` (`Usuario_idUsuario` ASC) ,
  INDEX `fk_Contacto_Rol1_idx` (`Rol_idRol` ASC) ,
  CONSTRAINT `fk_Contacto_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario` )
    REFERENCES `mydb`.`Usuario` (`idUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Contacto_Rol1`
    FOREIGN KEY (`Rol_idRol` )
    REFERENCES `mydb`.`Rol` (`idRol` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE  TABLE IF NOT EXISTS `mydb`.`Grupo` (
  `idGrupo` INT(11) NOT NULL AUTO_INCREMENT ,
  `nombreGrupo` VARCHAR(45) NOT NULL ,
  `descripcionGrupo` TINYTEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`idGrupo`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE  TABLE IF NOT EXISTS `mydb`.`Usuario_has_Grupo` (
  `Usuario_idUsuario` INT(11) NOT NULL ,
  `Grupos_idGrupo` INT(11) NOT NULL ,
  PRIMARY KEY (`Usuario_idUsuario`, `Grupos_idGrupo`) ,
  INDEX `fk_Usuario_has_Grupos_Grupos1_idx` (`Grupos_idGrupo` ASC) ,
  INDEX `fk_Usuario_has_Grupos_Usuario1_idx` (`Usuario_idUsuario` ASC) ,
  CONSTRAINT `fk_Usuario_has_Grupos_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario` )
    REFERENCES `mydb`.`Usuario` (`idUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_has_Grupos_Grupos1`
    FOREIGN KEY (`Grupos_idGrupo` )
    REFERENCES `mydb`.`Grupo` (`idGrupo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE  TABLE IF NOT EXISTS `mydb`.`Rol` (
  `idRol` INT(11) NOT NULL AUTO_INCREMENT ,
  `descripcionRol` VARCHAR(20) NULL DEFAULT NULL ,
  PRIMARY KEY (`idRol`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE  TABLE IF NOT EXISTS `mydb`.`Notificacion` (
  `idNotificacion` INT(11) NOT NULL AUTO_INCREMENT ,
  `Usuario_idUsuario` INT(11) NOT NULL ,
  `descripcionNotificacion` VARCHAR(256) NOT NULL ,
  PRIMARY KEY (`idNotificacion`) ,
  INDEX `fk_Notificacion_Usuario1` (`Usuario_idUsuario` ASC) ,
  CONSTRAINT `fk_Notificacion_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario` )
    REFERENCES `mydb`.`Usuario` (`idUsuario` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

USE `mydb`;

CREATE FUNCTION idUsuario() RETURNS INTEGER DETERMINISTIC NO SQL RETURN @id_select;

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`datos_busqueda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`datos_busqueda` (`idUsuario` INT, `nombreUsuario` INT, `apellidoUsuario` INT, `fotoUsuario` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`solicitudes_pendientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`solicitudes_pendientes` (`idUsuario` INT, `nombreUsuario` INT, `apellidoUsuario` INT, `fotoUsuario` INT);

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`lista_amigo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`lista_amigo` (`idUsuario` INT, `nombreUsuario` INT, `apellidoUsuario` INT, `fotoUsuario` INT, `Rol_idRol` INT);


USE `mydb`;

-- -----------------------------------------------------
-- View `mydb`.`datos_busqueda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`datos_busqueda`;
USE `mydb`;
CREATE  OR REPLACE VIEW `mydb`.`datos_busqueda` AS

select idUsuario, nombreUsuario, apellidoUsuario, fotoUsuario from usuario;


USE `mydb`;

-- -----------------------------------------------------
-- View `mydb`.`solicitudes_pendientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`solicitudes_pendientes`;
USE `mydb`;
CREATE  OR REPLACE VIEW `mydb`.`solicitudes_pendientes` AS

select idUsuario, nombreUsuario, apellidoUsuario, fotoUsuario from Usuario inner join Contacto where Usuario_idUsuario = idUsuario and estadoContacto = false and Usuario_idUsuario2 = id_Usuario();
;


USE `mydb`;

-- -----------------------------------------------------
-- View `mydb`.`lista_amigo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`lista_amigo`;
USE `mydb`;
CREATE  OR REPLACE VIEW `mydb`.`lista_amigo` AS
select idUsuario, nombreUsuario, apellidoUsuario, fotoUsuario, Rol_idRol from Usuario inner join Contacto where Usuario_idUsuario = idUsuario and estadoContacto = true and Usuario_idUsuario2 = id_Usuario()
union 
select idUsuario, nombreUsuario, apellidoUsuario, fotoUsuario, Rol_idRol from Usuario inner join Contacto where Usuario_idUsuario2 = idUsuario and estadoContacto = true and Usuario_idUsuario = id_Usuario();
;

-------------------------------------------------------
-- Datos Precargados
-------------------------------------------------------

USE mydb;

-- Insert de algunos roles prederminados 

INSERT INTO rol (idRol,descripcionRol) VALUES (1,'Amigo');
INSERT INTO rol (idRol,descripcionRol) VALUES (2,'Compañero');
INSERT INTO rol (idRol,descripcionRol) VALUES (3,'Compañero de trabajo');
INSERT INTO rol (idRol,descripcionRol) VALUES (4,'Mejor amigo');
INSERT INTO rol (idRol,descripcionRol) VALUES (5,'Familiar');
INSERT INTO rol (idRol,descripcionRol) VALUES (6,'Conyuge');
INSERT INTO rol (idRol,descripcionRol) VALUES (7,'Hijo');

-- Insert de algunos grupos, supuestamente creados

INSERT INTO grupo (idGrupo, nombreGrupo, descripcionGrupo) VALUES (1,'Ventas Buenos Aires','Venta de articulos de cualquier tipo');
INSERT INTO grupo (idGrupo, nombreGrupo, descripcionGrupo) VALUES (2,'Conocer gente nueva','Unete a nuestro grupo si deseas hacer nuevas amistades!!');
INSERT INTO grupo (idGrupo, nombreGrupo, descripcionGrupo) VALUES (3,'Recetas de cocina','Comunidad que comparte recetas de cocinas faciles');
INSERT INTO grupo (idGrupo, nombreGrupo, descripcionGrupo) VALUES (4,'Memes',NULL);



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
