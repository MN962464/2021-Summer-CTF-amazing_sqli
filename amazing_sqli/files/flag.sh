#!/bin/bash

mysql -e "CREATE DATABASE IF NOT EXISTS cometosql;USE cometosql; CREATE TABLE IF NOT EXISTS \`f_here_is_tips\` (\`hints\` varchar(100) NOT NULL) ENGINE=MyISAM  DEFAULT CHARSET=utf8;INSERT INTO \`f_here_is_tips\` VALUES ('$FLAG');" -uroot -proot

export FLAG=not_flag
FLAG=not_flag

rm -f /flag.sh
