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

/*Table structure for table `t_chn_stock_report` */

CREATE TABLE `t_chn_stock_report` (
  `nd` varchar(10) DEFAULT NULL,
  `jd` varchar(10) DEFAULT NULL,
  `code` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `eps` varchar(50) DEFAULT NULL COMMENT '每股收益',
  `eps_yoy` varchar(50) DEFAULT NULL COMMENT '每股收益同比(%)',
  `bvps` varchar(50) DEFAULT NULL COMMENT '每股净资产',
  `roe` varchar(50) DEFAULT NULL COMMENT '净资产收益率(%)',
  `epcf` varchar(50) DEFAULT NULL COMMENT '每股现金流量(元)',
  `net_profits` varchar(50) DEFAULT NULL COMMENT '净利润(万元)',
  `profits_yoy` varchar(50) DEFAULT NULL COMMENT '净利润同比(%)',
  `distrib` varchar(50) DEFAULT NULL COMMENT '分配方案',
  `report_date` varchar(30) DEFAULT NULL COMMENT '发布日期',
  KEY `idx_t_chn_stock_report` (`nd`,`jd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
