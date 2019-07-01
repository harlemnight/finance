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

/*Table structure for table `t_chn_stock_trade` */

CREATE TABLE `t_chn_stock_trade` (
  `datetime` varchar(30) DEFAULT NULL COMMENT '交易日期',
  `code` varchar(30) DEFAULT NULL COMMENT '代码',
  `open` varchar(30) DEFAULT NULL COMMENT '开盘价',
  `close` varchar(30) DEFAULT NULL COMMENT '收盘价',
  `high` varchar(30) DEFAULT NULL COMMENT '最高价',
  `low` varchar(30) DEFAULT NULL COMMENT '最低价',
  `vol` varchar(30) DEFAULT NULL COMMENT '成交量',
  `amount` varchar(30) DEFAULT NULL COMMENT '成交额',
  `tor` varchar(30) DEFAULT NULL COMMENT '换手率',
  `vr` varchar(30) DEFAULT NULL COMMENT '量比',
  `ma5` varchar(30) DEFAULT NULL COMMENT '5日均线',
  `ma10` varchar(30) DEFAULT NULL COMMENT '10日均线',
  `ma20` varchar(30) DEFAULT NULL COMMENT '20日均线',
  `ma60` varchar(30) DEFAULT NULL COMMENT '60日均线',
  KEY `IDX_T_CHN_STOCK_TRADE_CODE_RQ2` (`code`,`datetime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
