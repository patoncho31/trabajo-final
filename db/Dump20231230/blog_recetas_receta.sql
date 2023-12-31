-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recetas_receta`
--

DROP TABLE IF EXISTS `recetas_receta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas_receta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titulo` varchar(50) NOT NULL,
  `subtitulo` varchar(100) DEFAULT NULL,
  `resumen` varchar(200) DEFAULT NULL,
  `texto` longtext NOT NULL,
  `imagenes` varchar(100) DEFAULT NULL,
  `fecha` datetime(6) NOT NULL,
  `categorias_id` bigint DEFAULT NULL,
  `autor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `recetas_receta_categorias_id_dc7e5ddf_fk_recetas_categoria_id` (`categorias_id`),
  KEY `recetas_receta_autor_id_9388c5c2_fk_usuarios_usuario_id` (`autor_id`),
  CONSTRAINT `recetas_receta_autor_id_9388c5c2_fk_usuarios_usuario_id` FOREIGN KEY (`autor_id`) REFERENCES `usuarios_usuario` (`id`),
  CONSTRAINT `recetas_receta_categorias_id_dc7e5ddf_fk_recetas_categoria_id` FOREIGN KEY (`categorias_id`) REFERENCES `recetas_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas_receta`
--

LOCK TABLES `recetas_receta` WRITE;
/*!40000 ALTER TABLE `recetas_receta` DISABLE KEYS */;
INSERT INTO `recetas_receta` VALUES (1,'Pan',NULL,'Harina y agua','Harina y agua al horno','recetas/Pan-frances-1.png','2023-12-29 22:11:51.355184',1,2),(2,'empanadas','2','3','23','static/post_default.png','2023-12-30 05:23:39.084674',1,2);
/*!40000 ALTER TABLE `recetas_receta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-30 21:56:19
