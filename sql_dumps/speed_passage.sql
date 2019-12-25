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
-- Table structure for table `passage`
--

DROP TABLE IF EXISTS `passage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `passage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paragraph_id` int(11) NOT NULL,
  `paragraph` varchar(2000) NOT NULL,
  PRIMARY KEY (`id`,`paragraph_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passage`
--

LOCK TABLES `passage` WRITE;
/*!40000 ALTER TABLE `passage` DISABLE KEYS */;
INSERT INTO `passage` VALUES (1,1,'Mike and Morris lived in the same village. While Morris owned the largest jewelry shop in the village, Mike was a poor farmer. Both had large families with many sons, daughters-in-law and grandchildren. One fine day, Mike, tired of not being able to fed his family, decided to leave the village and move to the city where he was certain to earn enough to feed everyone.Along with his family, he left the village for the city. At night, they stopped under a large tree. There was a stream running nearby where they could freshen up themselves. He told his sons to clear the area below the tree, he told his wife to fetch water and he instructed his daughters-in-law to make up the fire and started cutting wood from the tree himself. They didn’t knew that in the branches of the tree, there was a thief hiding. He watched as Mike’s family worked together and also noticed that they had nothing to cook. Mike’s wife also thought the same and asked her husband ” Everything is ready but what shall we eat ? ” Mike raised his hands to heaven and said ” Don’t worry. He is watching all this from above. He will help us.”'),(1,2,'The thief got worried as he had seen that the family was large and worked well together. Taking advantage of the fact that they did not know he was hiding in the branches, he decided to make a quick escape. He climbed down safely when they were not looking and ran for his life. But, he left behind the bundle of stolen jewels and money which dropped into Mike’s lap. Mike opened it and jumped with joy when he saw the contents. The family gathered all their belongings and returned to the village. There was great excitement when they told everyone how they got rich.'),(1,3,'Morris thought that the tree was miraculous and this was a nice and quick way to earn some money. He ordered his family to pack some clothes and they set off as if on a journey. They also stopped under the same tree and Morris started commanding everyone as Mike had done. But no one in his family was willing to obey his orders. Being a rich family, they were used to having servants all around. So, the one who went to the river to fetch water enjoyed a nice bath. The one who went to get wood for fire went off to sleep. Morris’s wife said ” Everything is ready but what shall we eat ?” Morris raised his hands and said, ” Don’t worry. He is watching all this from above. He will help us.”'),(1,4,'As soon as he finished saying, the thief jumped down from the tree with a knife in hand. Seeing him, everyone started running here and there to save their lives. The thief stole everything they had and Morris and his family had to return to the village empty handed, having lost all their valuables that they had taken with them.');
/*!40000 ALTER TABLE `passage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-25 16:34:48
