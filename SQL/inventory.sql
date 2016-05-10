SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `inventory`
-- ----------------------------
DROP TABLE IF EXISTS `inventory`;
CREATE TABLE `inventory` (
  `id` int(10) NOT NULL,
  `slot1` varchar(255) DEFAULT NULL,
  `slot2` varchar(255) DEFAULT NULL,
  `slot3` varchar(255) DEFAULT NULL,
  `slot4` varchar(255) DEFAULT NULL,
  `slot5` varchar(255) DEFAULT NULL,
  `slot6` varchar(255) DEFAULT NULL,
  `slot7` varchar(255) DEFAULT NULL,
  `slot8` varchar(255) DEFAULT NULL,
  `slot9` varchar(255) DEFAULT NULL,
  `bank` bigint(20) DEFAULT '0',
  `class` varchar(255) DEFAULT 'no',
  PRIMARY KEY (`id`),
  CONSTRAINT `id` FOREIGN KEY (`id`) REFERENCES `userdata` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;