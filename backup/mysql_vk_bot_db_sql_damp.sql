-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `id_group` tinyint(4) DEFAULT NULL,
  `name_group` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES (1,'НПв-181'),(2,'Тестовая группа 1'),(3,'Тестовая группа 2');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marks`
--

DROP TABLE IF EXISTS `marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marks` (
  `id_mark` varchar(0) DEFAULT NULL,
  `name_subject` varchar(0) DEFAULT NULL,
  `student_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks`
--

LOCK TABLES `marks` WRITE;
/*!40000 ALTER TABLE `marks` DISABLE KEYS */;
/*!40000 ALTER TABLE `marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(14) DEFAULT NULL,
  `seq` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('timetable_temp',2),('students',50),('groups',3),('users',3);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `id_students` tinyint(4) DEFAULT NULL,
  `name` varchar(8) DEFAULT NULL,
  `surname` varchar(8) DEFAULT NULL,
  `patronymic` varchar(12) DEFAULT NULL,
  `student_number` int(11) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (0,'Максим','Кочетков','Владимирович',222034304,''),(1,'Сергей','Зайцев','Владимирович',123456789,''),(2,'Николай','Николаев','Олегович',8765876,''),(6,'Кристиан','Михайлов','Олегович',213423423,''),(38,'ggggg','hhhhh','jjjjj',5465462,''),(50,'Михаил','Козлов','Алексеевич',34234243,'');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable_temp`
--

DROP TABLE IF EXISTS `timetable_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timetable_temp` (
  `id_event_temp` tinyint(4) DEFAULT NULL,
  `text_event_temp` varchar(29) DEFAULT NULL,
  `date_event` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetable_temp`
--

LOCK TABLES `timetable_temp` WRITE;
/*!40000 ALTER TABLE `timetable_temp` DISABLE KEYS */;
INSERT INTO `timetable_temp` VALUES (0,'Тестовое временное событие №1','06.05.2022'),(1,'Тестовое временное событие №2','07.05.2022');
/*!40000 ALTER TABLE `timetable_temp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable_ussual`
--

DROP TABLE IF EXISTS `timetable_ussual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timetable_ussual` (
  `id_event_ussual` tinyint(4) DEFAULT NULL,
  `text_event_ussual` varchar(71) DEFAULT NULL,
  `group_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetable_ussual`
--

LOCK TABLES `timetable_ussual` WRITE;
/*!40000 ALTER TABLE `timetable_ussual` DISABLE KEYS */;
INSERT INTO `timetable_ussual` VALUES (10,'Всем привет! Сегодня у нас пара по искусственному интеллекту',1),(11,'Всем привет! Сегодня занятий нет :)',1),(20,'Всем привет! Сегодня занятий нет :)',1),(21,'Всем привет! Сегодня занятий нет :)',1),(30,'Всем привет! Сегодня у нас пара по английскому языку для слабой группы',1),(31,'Всем привет! Сегодня у нас пара по английскому языку для сильной группы',1),(40,'Всем привет! Сегодня занятий нет :)',1),(41,'Всем привет! Сегодня занятий нет :)',1),(50,'Всем привет! Сегодня занятий нет :)',1),(51,'Всем привет! Сегодня занятий нет :)',1),(60,'Всем привет! Сегодня у нас пары в MS Teams',1),(61,'Всем привет! Сегодня у нас очные пары в университете на орджо',1);
/*!40000 ALTER TABLE `timetable_ussual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id_user` tinyint(4) DEFAULT NULL,
  `login` varchar(6) DEFAULT NULL,
  `password` tinyint(4) DEFAULT NULL,
  `user_name` varchar(9) DEFAULT NULL,
  `user_role` tinyint(4) DEFAULT NULL,
  `user_group_id` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'max',1,'Максим',1,''),(2,'sergo',2,'Сергей',2,'2'),(3,'nastya',3,'Анастасия',2,'1');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:26
