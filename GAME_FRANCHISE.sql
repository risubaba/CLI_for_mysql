
-- NOTES:
-- In 1:M relationship we can add FK to M side
-- Issue is in M:1 relationship where FK has been added to 1 side in SRS

-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Company
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

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
-- Table structure for table `DEPARTMENT`
--
DROP DATABASE IF EXISTS `Franchise`;
CREATE SCHEMA `Franchise`;
USE `Franchise`;
DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employee_id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  `salary` int(10) NOT NULL,
  `address_line1` varchar(100) NOT NULL,
  `address_line2` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('9999999999', 'John', 'john.smith@gmail.com', '1000000', '420 Highway Lane', 'Texas'),('8888888888',	'Smith',	'smith.john@gmail.com',	'100000',	'69 Road', 'LA');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `phone_num_emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phone_num_emp` (
  `employee_id` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  PRIMARY KEY (`phone_num`),
  CONSTRAINT `phone_num_esp_fk` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `phone_num_emp` WRITE;
/*!40000 ALTER TABLE `phone_num_emp` DISABLE KEYS */;
INSERT INTO `phone_num_emp` VALUES ('9999999999', '9898989898'),('8888888888', '8787878787');
/*!40000 ALTER TABLE `phone_num_emp` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `dependent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dependent` (
  `employee_id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `relationship_type` varchar(100) NOT NULL,
  PRIMARY KEY (`employee_id`,`name`,`relationship_type`),
  CONSTRAINT `dependent_fk` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `dependent` WRITE;
/*!40000 ALTER TABLE `dependent` DISABLE KEYS */;
INSERT INTO `dependent` VALUES ('9999999999', 'Johnson', 'son'),('8888888888', 'Smithson', 'son');
/*!40000 ALTER TABLE `dependent` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customer_id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_address` varchar(50) DEFAULT NULL,
  `address_line1` varchar(100) NOT NULL,
  `address_line2` varchar(100) DEFAULT NULL,
  `age` int(2) DEFAULT NULL,
  `date_of_birth` date NOT NULL,
  `employee_id` varchar(50) NOT NULL,
  PRIMARY KEY (`customer_id`),
  CONSTRAINT `interacts_fk` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('7777777777', 'Nonidh',	'nonidh.singh@iiit.com', '420 Bakul Nivas',	'IIIT Hyderabad', '50' , '30-2-1969',	'9999999999'),('6666666666', 'Rohan', 'rohan.chako@iiit.com',	'69 Bakul Nivas', 'IIIT Hyderabad',	'50', '30-2-1969', '9999999999');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `phone_num_cus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phone_num_cus` (
  `customer_id` varchar(50) NOT NULL,
  `phone_num` varchar(50)  NOT NULL,
  PRIMARY KEY (`phone_num`),
  CONSTRAINT `phone_num_cus_fk` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `phone_num_cus` WRITE;
/*!40000 ALTER TABLE `phone_num_cus` DISABLE KEYS */;
INSERT INTO `phone_num_cus` VALUES ('7777777777', '987654321'),('6666666666', '9988776655');
/*!40000 ALTER TABLE `phone_num_cus` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehicle` (
  `customer_id` varchar(50) UNIQUE NOT NULL,
  `vehicle_license_plate` varchar(100) NOT NULL,
  PRIMARY KEY (`vehicle_license_plate`),
  `vehicle_model` varchar(100) NOT NULL,
  CONSTRAINT `vehicle_fk` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES ('7777777777', 'AA-BB-CC', 'Mercedes'),('6666666666', 'XX-YY-ZZ', 'Audi');
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `store` (
  `store_id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  `website_address` varchar(100) DEFAULT NULL,
  `customer_service_website_address` varchar(100) DEFAULT NULL,
  `location` varchar(100) NOT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES ('3333333333',	'Palash',	'palash@nivas.com',	'www.nivas.com/palash',	'www.service.nivas.com/palash',	'Hyderabad'), ('2222222222', 'Kadamb', 'kadamb@nivas.com', 'www.nivas.com/kadamb', 'www.service.nivas.com/kadamb', 'Gurgaon');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `product_id` varchar(50) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `num_in_stock` varchar(50) DEFAULT NULL,
  `price` varchar(50) NOT NULL,
  `store_id` varchar(50) NOT NULL,
  PRIMARY KEY (`product_id`),
  CONSTRAINT `has_fk` FOREIGN KEY (`store_id`) REFERENCES `store` (`store_id`)
  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('5555555555', 'CS:GO', '100', '500', '3333333333'),('4444444444', 'FIFA', '10', '3000', '2222222222');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `games` (
  `product_id` varchar(50) UNIQUE NOT NULL,
  `developer` varchar(50) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `platform` varchar(50) NOT NULL,
  `release_date` date NOT NULL,
  `esrb_rating` varchar(3) NOT NULL,
  PRIMARY KEY (`product_id`),
  CONSTRAINT `subclass_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
  ON DELETE CASCADE
  -- CONSTRAINT `sells_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES ('5555555555', 'valve', 'FPS', 'PC', '1-1-2000', '6.9'), ('4444444444', 'EA', 'Sports', 'PS4', '2-2-2000', '9.6');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `sells`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sells` (
  `employee_id` varchar(50) NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  `store_id` varchar(50) NOT NULL,
  `product_id` varchar(50) NOT NULL,
  `total_price` varchar(50) NOT NULL,
  PRIMARY KEY (`store_id`,`employee_id`,`product_id`,`customer_id`),
  CONSTRAINT `e_fk` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE,
  CONSTRAINT `c_fk` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE,
  CONSTRAINT `s_fk` FOREIGN KEY (`store_id`) REFERENCES `store` (`store_id`) ON DELETE CASCADE,
  CONSTRAINT `p_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `sells` WRITE;
/*!40000 ALTER TABLE `sells` DISABLE KEYS */;
INSERT INTO `sells` VALUES ('9999999999', '7777777777', '3333333333', '4444444444', '3000'), ('8888888888', '6666666666', '2222222222', '5555555555', '500');
/*!40000 ALTER TABLE `sells` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `e_id1` varchar(50) NOT NULL,
  `e_id2` varchar(50) NOT NULL,
  `timestamp` timestamp NOT NULL,
  `message` varchar(50) NOT NULL,
  PRIMARY KEY (`E_id1`,`E_id2`,`Timestamp`),
  CONSTRAINT `e1_fk` FOREIGN KEY (`e_id1`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE,
  CONSTRAINT `e2_fk` FOREIGN KEY (`e_id2`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES ('9999999999', '8888888888', '2019-11-13 06:03:47', 'Hi! Wanna grab a coffee sometime?'), ('8888888888', '9999999999', '2019-11-13 06:03:48', 'No');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

-- /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
-- /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
-- /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
-- /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
-- /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
-- /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- -- Dump completed on 2018-08-12 23:29:32
