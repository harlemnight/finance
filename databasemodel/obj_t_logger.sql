/*
SQLyog Ultimate
MySQL - 5.7.20-log : Database - db_finance
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_finance` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `db_finance`;

/*Table structure for table `t_logger` */

CREATE TABLE `t_logger` (
  `id` bigint(30) NOT NULL AUTO_INCREMENT,
  `code` varchar(30) DEFAULT NULL,
  `operation` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `content` varchar(500) DEFAULT NULL,
  `lrrq` varchar(30) NOT NULL,
  `ywlx` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_t_logger_lrrq` (`lrrq`)
) ENGINE=InnoDB AUTO_INCREMENT=248884 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
