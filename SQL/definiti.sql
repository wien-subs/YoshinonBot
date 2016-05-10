SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `definiti`
-- ----------------------------
DROP TABLE IF EXISTS `definiti`;
CREATE TABLE `definiti` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `cuvant` varchar(200) NOT NULL,
  `definitie` text NOT NULL,
  `data` varchar(100) NOT NULL,
  `autor` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
