/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 100113
Source Host           : localhost:3306
Source Database       : botproject

Target Server Type    : MYSQL
Target Server Version : 100113
File Encoding         : 65001

Date: 2016-12-11 20:40:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for blacklist
-- ----------------------------
DROP TABLE IF EXISTS `blacklist`;
CREATE TABLE `blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for definiti
-- ----------------------------
DROP TABLE IF EXISTS `definiti`;
CREATE TABLE `definiti` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `cuvant` varchar(200) NOT NULL,
  `definitie` text NOT NULL,
  `data` varchar(100) NOT NULL,
  `autor` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for inventory
-- ----------------------------
DROP TABLE IF EXISTS `inventory`;
CREATE TABLE `inventory` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `userid` int(10) NOT NULL,
  `slot0` varchar(255) DEFAULT 'empty',
  `slot1` varchar(255) DEFAULT 'empty',
  `slot2` varchar(255) DEFAULT 'empty',
  `slot3` varchar(255) DEFAULT 'empty',
  `slot4` varchar(255) DEFAULT 'empty',
  `slot5` varchar(255) DEFAULT 'empty',
  `slot6` varchar(255) DEFAULT 'empty',
  `slot7` varchar(255) DEFAULT 'empty',
  `slot8` varchar(255) DEFAULT 'empty',
  `slot9` varchar(255) DEFAULT 'empty',
  `avatar` varchar(255) DEFAULT 'no',
  `level` int(2) DEFAULT '0',
  `xp` int(3) DEFAULT '0' COMMENT '0',
  `class` int(1) DEFAULT '0',
  `power` int(10) DEFAULT '0',
  `hp` int(10) DEFAULT '0',
  `helmet` varchar(255) DEFAULT 'no',
  `chestplate` varchar(255) DEFAULT 'no',
  `leftarm` varchar(255) DEFAULT 'no',
  `rightarm` varchar(255) DEFAULT 'no',
  `leggis` varchar(255) DEFAULT 'no',
  `boots` varchar(255) DEFAULT 'no',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `desc` text NOT NULL,
  `class` varchar(255) NOT NULL,
  `meta-attack` int(3) DEFAULT NULL,
  `meta-hp` int(3) DEFAULT NULL,
  `price` int(3) DEFAULT NULL,
  `price-sell` int(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for setting
-- ----------------------------
DROP TABLE IF EXISTS `setting`;
CREATE TABLE `setting` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for userdata
-- ----------------------------
DROP TABLE IF EXISTS `userdata`;
CREATE TABLE `userdata` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) NOT NULL,
  `money` bigint(200) DEFAULT NULL,
  `access` int(2) NOT NULL DEFAULT '1',
  `firstjoin` varchar(255) NOT NULL,
  `lastmoney` bigint(255) DEFAULT NULL,
  `lastzar` bigint(255) DEFAULT '10',
  `laststeal` bigint(255) DEFAULT '1',
  `battle` int(4) DEFAULT '0',
  `win` int(3) DEFAULT '0',
  `lose` int(3) DEFAULT '0',
  `bank` bigint(255) DEFAULT '0',
  `battlecd` bigint(255) NOT NULL DEFAULT '20',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=922 DEFAULT CHARSET=latin1;
