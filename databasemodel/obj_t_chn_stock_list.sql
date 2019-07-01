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

/*Table structure for table `t_chn_stock_list` */

CREATE TABLE `t_chn_stock_list` (
  `code` varchar(20) DEFAULT NULL COMMENT '代码',
  `name` varchar(20) DEFAULT NULL COMMENT '名称',
  `industry` varchar(20) DEFAULT NULL COMMENT '所属行业',
  `area` varchar(20) DEFAULT NULL COMMENT '地区',
  `pe` varchar(20) DEFAULT NULL COMMENT '市盈率',
  `outstanding` varchar(30) DEFAULT NULL COMMENT '流通股本(亿)',
  `totals` varchar(30) DEFAULT NULL COMMENT '总股本(亿)',
  `totalAssets` varchar(30) DEFAULT NULL COMMENT '总资产(万)',
  `liquidAssets` varchar(30) DEFAULT NULL COMMENT '流动资产',
  `fixedAssets` varchar(30) DEFAULT NULL COMMENT '固定资产',
  `reserved` varchar(30) DEFAULT NULL COMMENT '公积金',
  `reservedPerShare` varchar(30) DEFAULT NULL COMMENT '每股公积金',
  `esp` varchar(30) DEFAULT NULL COMMENT '每股收益',
  `bvps` varchar(30) DEFAULT NULL COMMENT '每股净资',
  `pb` varchar(330) DEFAULT NULL COMMENT '市净率',
  `timeToMarket` varchar(20) DEFAULT NULL COMMENT '上市日期',
  `undp` varchar(30) DEFAULT NULL COMMENT '未分利润',
  `perundp` varchar(30) DEFAULT NULL COMMENT '每股未分配',
  `rev` varchar(20) DEFAULT NULL COMMENT '收入同比(%)',
  `profit` varchar(20) DEFAULT NULL COMMENT '利润同比(%)',
  `gpr` varchar(20) DEFAULT NULL COMMENT '毛利率(%)',
  `npr` varchar(20) DEFAULT NULL COMMENT '净利润率(%)',
  `holders` varchar(30) DEFAULT NULL COMMENT '股东人数',
  KEY `IDX_T_CHN_STOCK_LIST_CODE` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
