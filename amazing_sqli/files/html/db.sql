CREATE DATABASE IF NOT EXISTS cometosql;

USE cometosql;

CREATE TABLE IF NOT EXISTS `come_on` (
  `id` int(10) NOT NULL,
  `data` varchar(20) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


INSERT INTO `come_on` values(1,'here_is_nothing'),(2,'is'),(3,'nothing');
CREATE TABLE IF NOT EXISTS `e_see_the_tips`(
  `hints` varchar(100) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


INSERT INTO `e_see_the_tips` values('here_is_still_nothing'),('is'),('still')('nothing');
CREATE TABLE IF NOT EXISTS `z_search_the_tips`(
  `hints` varchar(100) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


INSERT INTO `z_search_the_tips` values('you_are_cheated'),('is'),('still')('nothing');
CREATE TABLE IF NOT EXISTS `d_here_is_tip`(
  `hints` varchar(100) NOT NULL
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


INSERT INTO `d_here_is_tip` values('just_a_joke'),('is'),('still')('nothing');
