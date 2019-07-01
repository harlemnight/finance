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

/*Table structure for table `t_chn_stock_cashflow` */

CREATE TABLE `t_chn_stock_cashflow` (
  `nd` varchar(10) DEFAULT NULL,
  `jd` varchar(10) DEFAULT NULL,
  `code` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `cf_sales` varchar(50) DEFAULT NULL COMMENT '经营现金净流量对销售收入比率',
  `rateofreturn` varchar(50) DEFAULT NULL COMMENT '资产的经营现金流量回报率',
  `cf_nm` varchar(50) DEFAULT NULL COMMENT '经营现金净流量与净利润的比率',
  `cf_liabilities` varchar(50) DEFAULT NULL COMMENT '经营现金净流量对负债比率',
  `cashflowratio` varchar(50) DEFAULT NULL COMMENT '现金流量比率',
  KEY `idx_t_chn_stock_cashflow` (`nd`,`jd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
