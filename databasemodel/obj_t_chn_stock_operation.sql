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

/*Table structure for table `t_chn_stock_operation` */

CREATE TABLE `t_chn_stock_operation` (
  `nd` varchar(10) DEFAULT NULL,
  `jd` varchar(10) DEFAULT NULL,
  `code` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `arturnover` varchar(50) DEFAULT NULL COMMENT '应收账款周转率(次)',
  `arturndays` varchar(50) DEFAULT NULL COMMENT '应收账款周转天数(天)',
  `inventory_turnover` varchar(50) DEFAULT NULL COMMENT '存货周转率(次)',
  `inventory_days` varchar(50) DEFAULT NULL COMMENT '存货周转天数(天)',
  `currentasset_turnover` varchar(50) DEFAULT NULL COMMENT '流动资产周转率(次)',
  `currentasset_days` varchar(50) DEFAULT NULL COMMENT '流动资产周转天数(天)',
  KEY `idx_t_chn_stock_operation` (`nd`,`jd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
