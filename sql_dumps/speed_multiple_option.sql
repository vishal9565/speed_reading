-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: speed
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `multiple_option`
--

DROP TABLE IF EXISTS `multiple_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `multiple_option` (
  `version_id` bigint(20) unsigned NOT NULL,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_updated_on` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_updated_by` varchar(255) DEFAULT 'SYSTEM',
  `question_id` bigint(20) DEFAULT NULL,
  `option_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `option_text` varchar(200) NOT NULL,
  PRIMARY KEY (`option_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `multiple_option_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `multiple_option`
--

LOCK TABLES `multiple_option` WRITE;
/*!40000 ALTER TABLE `multiple_option` DISABLE KEYS */;
INSERT INTO `multiple_option` VALUES (1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',1,1,'Being a large family, they knew that they could easily defeat the thief'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',1,2,'It was a convenient spot for taking a halt at night'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',1,3,'There was a stream nearby and wood enough to build a house'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',1,4,'That was the only large tree that could shelter their large family'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',2,5,'He was a rich businessman'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',2,6,'He bullied his wife'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',2,7,'He paid his servants well'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',2,8,'He was greedy and imitated Mike'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',3,9,'Being a large family, they knew that they could easily defeat the thief'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',3,10,'It was a convenient spot for taking a halt at night'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',3,11,'There was a stream nearby and wood enough to build a house'),(1,'2019-12-28 07:49:20','2019-12-28 07:49:20','SYSTEM',3,12,'That was the only large tree that could shelter their large family');
/*!40000 ALTER TABLE `multiple_option` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-28 13:20:27
