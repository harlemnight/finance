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

/*Table structure for table `t_chn_stock_winer` */

CREATE TABLE `t_chn_stock_winer` (
  `datetime` varchar(30) DEFAULT NULL,
  `code` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `pchange` varchar(50) DEFAULT NULL COMMENT '当日涨跌幅',
  `amount` varchar(50) DEFAULT NULL COMMENT '龙虎榜成交额(万)',
  `buy` varchar(50) DEFAULT NULL COMMENT '买入额(万)',
  `sell` varchar(50) DEFAULT NULL COMMENT '卖出额(万)',
  `reason` varchar(100) DEFAULT NULL COMMENT '上榜原因',
  `bratio` varchar(50) DEFAULT NULL COMMENT '买入占总成交比例',
  `sratio` varchar(50) DEFAULT NULL COMMENT '卖出占总成交比例',
  `date` varchar(50) DEFAULT NULL COMMENT '日期',
  KEY `idx_t_chn_stock_winer` (`datetime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
