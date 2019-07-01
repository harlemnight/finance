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

/*Table structure for table `t_chn_index_list` */

CREATE TABLE `t_chn_index_list` (
  `code` varchar(30) NOT NULL COMMENT '指数代码',
  `name` varchar(30) DEFAULT NULL COMMENT '指数名称',
  `change` varchar(30) DEFAULT NULL COMMENT '涨跌幅',
  `open` varchar(30) DEFAULT NULL COMMENT '开盘点位',
  `preclose` varchar(30) DEFAULT NULL COMMENT '昨日收盘点位',
  `close` varchar(30) DEFAULT NULL COMMENT '收盘点位',
  `high` varchar(30) DEFAULT NULL COMMENT '最高点位',
  `low` varchar(30) DEFAULT NULL COMMENT '最低点位',
  `volume` varchar(50) DEFAULT NULL COMMENT '成交量(手)',
  `amount` varchar(50) DEFAULT NULL COMMENT '成交金额（亿元）',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
