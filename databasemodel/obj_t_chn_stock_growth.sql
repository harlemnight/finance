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

/*Table structure for table `t_chn_stock_growth` */

CREATE TABLE `t_chn_stock_growth` (
  `nd` varchar(10) DEFAULT NULL,
  `jd` varchar(10) DEFAULT NULL,
  `code` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `mbrg` varchar(50) DEFAULT NULL COMMENT '主营业务收入增长率(%)',
  `nprg` varchar(50) DEFAULT NULL COMMENT '净利润增长率(%)',
  `nav` varchar(50) DEFAULT NULL COMMENT '净资产增长率',
  `targ` varchar(50) DEFAULT NULL COMMENT '总资产增长率',
  `epsg` varchar(50) DEFAULT NULL COMMENT '每股收益增长率',
  `seg` varchar(50) DEFAULT NULL COMMENT '股东权益增长率',
  KEY `idx_t_chn_stock_growth` (`nd`,`jd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
