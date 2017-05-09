/*
Source Server         : WS BotChatango
Source Server Version : 100029
Source Host           : HiddenByAdmin
Source Database       : ws_BotProject
Target Server Type    : MYSQL
Date: 2017-05-09 19:21:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for announce
-- ----------------------------
DROP TABLE IF EXISTS `announce`;
CREATE TABLE `announce` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `text` text,
  `count` int(3) DEFAULT '1',
  `max` int(3) DEFAULT NULL,
  `data` varchar(50) DEFAULT NULL,
  `enable` int(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

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
  `helmet` int(2) DEFAULT '0',
  `chestplate` int(2) DEFAULT '0',
  `leftarm` int(2) DEFAULT '0',
  `rightarm` int(2) DEFAULT '0',
  `leggis` int(2) DEFAULT '0',
  `boots` int(2) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `desc` text NOT NULL,
  `slot` int(1) NOT NULL DEFAULT '0',
  `class` int(1) NOT NULL,
  `meta-attack` int(3) DEFAULT NULL,
  `meta-hp` int(3) DEFAULT NULL,
  `price` int(3) DEFAULT NULL,
  `price-sell` int(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

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
) ENGINE=InnoDB AUTO_INCREMENT=1479 DEFAULT CHARSET=latin1;
