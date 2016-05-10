SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `userdata`
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
  `helmet` int(2) DEFAULT '0',
  `chestplate` int(2) DEFAULT '0',
  `leggs` int(2) DEFAULT '0',
  `boots` int(2) DEFAULT '0',
  `righthand` int(2) DEFAULT '0',
  `lefthand` int(2) DEFAULT '0',
  `battle` int(4) DEFAULT '0',
  `win` int(3) DEFAULT '0',
  `lose` int(3) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;