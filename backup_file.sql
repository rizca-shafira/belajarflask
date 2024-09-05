-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: ayopy
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbayoadmin`
--

DROP TABLE IF EXISTS `tbayoadmin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbayoadmin` (
  `no_anggota` int NOT NULL AUTO_INCREMENT,
  `nama_anggota` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`no_anggota`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbayoadmin`
--

LOCK TABLES `tbayoadmin` WRITE;
/*!40000 ALTER TABLE `tbayoadmin` DISABLE KEYS */;
INSERT INTO `tbayoadmin` VALUES (3,'tesadmin49','admin@gmail.com'),(4,'admin22','rizca@gmail.com');
/*!40000 ALTER TABLE `tbayoadmin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbayoanggota`
--

DROP TABLE IF EXISTS `tbayoanggota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbayoanggota` (
  `no_anggota` int NOT NULL AUTO_INCREMENT,
  `nama_anggota` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`no_anggota`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbayoanggota`
--

LOCK TABLES `tbayoanggota` WRITE;
/*!40000 ALTER TABLE `tbayoanggota` DISABLE KEYS */;
INSERT INTO `tbayoanggota` VALUES (5,'cicaa','cici@gmail.comm'),(6,'risca','ris@yahoo.com');
/*!40000 ALTER TABLE `tbayoanggota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbayotransaksi`
--

DROP TABLE IF EXISTS `tbayotransaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbayotransaksi` (
  `kode_transaksi` int NOT NULL AUTO_INCREMENT,
  `no_anggota` int DEFAULT NULL,
  `no_admin` int DEFAULT NULL,
  `nama_barang` varchar(255) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `harga` int DEFAULT NULL,
  PRIMARY KEY (`kode_transaksi`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbayotransaksi`
--

LOCK TABLES `tbayotransaksi` WRITE;
/*!40000 ALTER TABLE `tbayotransaksi` DISABLE KEYS */;
INSERT INTO `tbayotransaksi` VALUES (1,5,3,'barag',1,200012),(2,5,3,'barang',2,30000),(3,5,3,'brg2',4,12000),(7,17,4,'sepatu',4,31000);
/*!40000 ALTER TABLE `tbayotransaksi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-06  1:59:17
