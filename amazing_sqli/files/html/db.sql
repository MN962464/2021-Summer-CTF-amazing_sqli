CREATE DATABASE IF NOT EXISTS cometosql;

USE cometosql;

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `user` char(11) NOT NULL COMMENT '用户名',
  `pass` char(11) NOT NULL COMMENT '密码',
  `email` char(100) NOT NULL COMMENT '电子邮件',
  PRIMARY KEY (`user`,`pass`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


INSERT INTO `users` values('admin','55678@@','mai_ning@cuc.edu.cn');

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
