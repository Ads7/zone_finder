"subzone_id","zone_id","name","latitude","longitude","active_flag"

CREATE TABLE subzone (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  expired_date DATE NOT NULL,
  amount DECIMAL(10,2) NULL,
  PRIMARY KEY (id)
);
DROP TABLE IF EXISTS `zones`;
CREATE TABLE IF NOT EXISTS `zones` (
  `zone_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `state_id` smallint(3) unsigned DEFAULT NULL,
  `city_id` smallint(3) unsigned NOT NULL ,
  `real_city` varchar(30) NOT NULL,
  `latitude` decimal(20,16) NOT NULL DEFAULT '0.0000000000000000',
  `longitude` decimal(20,16) NOT NULL DEFAULT '0.0000000000000000',
   PRIMARY KEY (`zone_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `subzones`;
CREATE TABLE IF NOT EXISTS `subzones` (
  `subzone_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `zone_id` smallint(5) unsigned NOT NULL ,
  `name` varchar(30) NOT NULL,
  `latitude` decimal(20,16) NOT NULL DEFAULT '0.0000000000000000',
  `longitude` decimal(20,16) NOT NULL DEFAULT '0.0000000000000000',
  `active_flag` smallint(1) unsigned NOT NULL,
   PRIMARY KEY (`subzone_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

LOAD DATA LOCAL INFILE '/home/user/workspace/zonefinder/zones_WA_state.csv' 
INTO TABLE zones
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;