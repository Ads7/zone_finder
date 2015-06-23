-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u1
-- http://www.phpmyadmin.net
--
-- Host: 10.0.117.22
-- Generation Time: Jun 23, 2015 at 11:22 AM
-- Server version: 5.6.24
-- PHP Version: 5.4.39-0+deb7u2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `zomato4`
--

-- --------------------------------------------------------

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
CREATE TABLE IF NOT EXISTS `cities` (
  `city_id` smallint(3) unsigned NOT NULL AUTO_INCREMENT,
  `state_id` smallint(3) unsigned DEFAULT NULL,
  `name` varchar(30) NOT NULL,
  `display_order` smallint(3) unsigned NOT NULL,
  `default_language_id` tinyint(3) unsigned NOT NULL DEFAULT '1',
  `language_id` tinyint(3) unsigned NOT NULL DEFAULT '1',
  `country_id` tinyint(3) unsigned NOT NULL,
  `metro_city_id` smallint(3) unsigned NOT NULL,
  `is_town` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `is_state` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `std_code` varchar(8) NOT NULL,
  `url` varchar(40) NOT NULL,
  `active_flag` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `admin_active_flag` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `has_dc_team` tinyint(1) unsigned NOT NULL,
  `has_restaurants` tinyint(1) unsigned NOT NULL,
  `has_nightlife` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `has_chillout` tinyint(4) NOT NULL,
  `has_takeaway` tinyint(1) unsigned NOT NULL,
  `has_cafes` tinyint(1) unsigned NOT NULL,
  `has_events` tinyint(1) unsigned NOT NULL,
  `has_45_star` tinyint(3) unsigned NOT NULL,
  `has_dish_search` tinyint(1) unsigned NOT NULL,
  `has_postcode_search` tinyint(1) unsigned NOT NULL,
  `has_pyd` tinyint(1) unsigned NOT NULL,
  `has_uber_integration` tinyint(1) unsigned NOT NULL,
  `has_nye_events` tinyint(1) unsigned NOT NULL,
  `filter_luxury_dining` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_michelin_starred` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `has_catering` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `latitude` decimal(20,16) NOT NULL DEFAULT '0.0000000000000000',
  `longitude` decimal(20,16) NOT NULL DEFAULT '0.0000000000000000',
  `distance_unit` enum('km','mi') NOT NULL DEFAULT 'km',
  `search_radius` decimal(5,2) NOT NULL DEFAULT '2.50',
  `citibank_discount_flag` tinyint(1) unsigned NOT NULL,
  `emirates_discount_flag` tinyint(1) unsigned NOT NULL,
  `show_zones` tinyint(1) unsigned NOT NULL,
  `cft_ranges` varchar(500) NOT NULL COMMENT 'city specific ranges for cost for two search filters',
  `cft_ranges_web` text NOT NULL COMMENT 'City specific ranges for cost for two search filters (for Web)',
  `cft_round_off` int(5) unsigned NOT NULL DEFAULT '1',
  `numeric_cft` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `meal_timings` varchar(250) NOT NULL DEFAULT '{breakfast:"0300-1100",lunch:"1101-1500",dinner:"1501-0259"}',
  `menus_active_flag` tinyint(1) unsigned NOT NULL,
  `photos_active_flag` tinyint(1) unsigned NOT NULL,
  `reviews_active_flag` tinyint(1) unsigned NOT NULL,
  `maps_active_flag` tinyint(1) unsigned NOT NULL,
  `review_alert_email` varchar(100) NOT NULL DEFAULT '',
  `qc_email` varchar(50) NOT NULL,
  `filter_veg` tinyint(1) unsigned NOT NULL,
  `filter_serves_veg` tinyint(1) unsigned NOT NULL,
  `filter_non_veg` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `show_non_veg` tinyint(1) unsigned NOT NULL COMMENT 'tells whether non veg details are important for this city and should be displayed on the interface',
  `filter_credit_cards` tinyint(1) unsigned NOT NULL,
  `filter_buffet` tinyint(1) unsigned NOT NULL,
  `filter_happy_hours` tinyint(1) unsigned NOT NULL,
  `filter_wifi` tinyint(1) unsigned NOT NULL,
  `filter_breakfast` tinyint(1) unsigned NOT NULL,
  `filter_bar` tinyint(1) unsigned NOT NULL,
  `filter_no_bar` tinyint(1) unsigned NOT NULL,
  `filter_live_music` tinyint(1) unsigned NOT NULL,
  `filter_outdoor_seating` tinyint(1) unsigned NOT NULL,
  `filter_garden` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_has_events` tinyint(1) unsigned NOT NULL,
  `filter_sheesha` tinyint(1) unsigned NOT NULL,
  `filter_halal` tinyint(1) unsigned NOT NULL,
  `filter_friday_brunch` tinyint(1) unsigned NOT NULL,
  `filter_sunday_brunch` tinyint(1) unsigned NOT NULL,
  `filter_weekend_brunch` tinyint(1) NOT NULL DEFAULT '0',
  `filter_sports_bar` tinyint(1) unsigned NOT NULL,
  `filter_offers` tinyint(3) unsigned NOT NULL,
  `check_cookie_flag` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `acd_active_flag` tinyint(1) unsigned NOT NULL,
  `filter_desserts_bakes` tinyint(1) unsigned NOT NULL,
  `rooftop_flag` tinyint(1) NOT NULL,
  `afternoon_tea_flag` tinyint(1) NOT NULL,
  `cafe_flag` tinyint(1) NOT NULL DEFAULT '0',
  `quick_bites_flag` tinyint(1) unsigned NOT NULL,
  `filter_wishlist` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_pet_friendly` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_cheap_eats` tinyint(1) unsigned NOT NULL,
  `filter_vineyard` tinyint(1) unsigned NOT NULL,
  `filter_seaside` tinyint(1) NOT NULL DEFAULT '0',
  `has_collections` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_collections` tinyint(1) NOT NULL,
  `has_acd` tinyint(1) NOT NULL DEFAULT '0',
  `has_tablebooking` tinyint(1) NOT NULL DEFAULT '0',
  `level_one_mailer` tinyint(1) unsigned NOT NULL,
  `level_two_mailer` tinyint(1) unsigned NOT NULL,
  `filter_lunch_menu` tinyint(1) unsigned NOT NULL,
  `filter_debit_card` tinyint(1) unsigned NOT NULL,
  `filter_brunch` tinyint(1) unsigned NOT NULL,
  `filter_sports_tv` tinyint(1) unsigned NOT NULL,
  `filter_patio_seating` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_wheelchair` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_chains` tinyint(1) unsigned NOT NULL,
  `filter_gluten_free` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_healthy_food` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_vegetarian_friendly` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_all_you_can_eat` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_night_clubs` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_early_bird` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_child_friendly` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_beach_side` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_smoking_area` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_smoke_free_area` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_beer_from_tank` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_disabled_friendly` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_byob` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `banner_type` enum('image','text') NOT NULL DEFAULT 'text',
  `time_difference` mediumint(9) NOT NULL DEFAULT '0',
  `has_daily_menus` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_meal_coupon` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_vegan` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_board_games` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_catering` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_generator` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_live_sports_screening` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_kosher` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_byow` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_byowb` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_kids_area` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_live_entertainment` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_group_meal` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_exclude_mall` tinyint(1) unsigned DEFAULT '0',
  `filter_ramadan` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_iftar` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_suhoor` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `filter_karak` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `migrated_from` varchar(30) DEFAULT NULL,
  `tier` smallint(6) NOT NULL DEFAULT '0',
  `city_highlighter` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`city_id`),
  KEY `ix_url` (`url`),
  KEY `hasNightlife` (`has_nightlife`),
  KEY `active_flag` (`active_flag`),
  KEY `ix_displayOrder` (`display_order`),
  KEY `tier` (`tier`),
  KEY `name` (`name`),
  KEY `idx_country_id` (`country_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=11053 ;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`city_id`, `name`, `state_id`, `active_flag`, `latitude`, `longitude`) VALUES
(279, 'Seattle', 115, 1, 47.6057700000000000, -122.3294370000000000),
(1240, 'Spokane', 115, 1, 47.6808652109704950, -117.4061756244730100),
(1243, 'Washington State', 115, 0, 47.0654215333585950, -120.7526882668680200),
(1246, 'Yakima', 115, 1, 46.5986853011583050, -120.5265928571430000),
(1249, 'Olympia', 115, 1, 47.0385301760564050, -122.8874269049300100),
(1252, 'Bellingham', 115, 1, 48.7578117313019000, -122.4762855207759900),
(9874, 'Arlington, Washington State', 115, 1, 48.1705540625000000, -122.1631167135000000),
(9875, 'Sultan', 115, 1, 47.8641361606000000, -121.7958788848000000),
(9876, 'Gold Bar', 115, 1, 47.8540441000000000, -121.6958905600000000),
(9877, 'Darrington', 115, 1, 48.2572426125000000, -121.5981968750000000),
(9878, 'Granite Falls, Washington Stat', 115, 1, 48.0833222130000000, -121.9704753478000000),
(9879, 'Camano Island', 115, 1, 48.2235584000000000, -122.4652182000000000),
(9880, 'Stanwood', 115, 1, 48.2407278383000000, -122.3503034733000000),
(9881, 'Allyn', 115, 1, 47.3781254000000000, -122.8377520000000000),
(9882, 'Pacific Beach', 115, 1, 47.2072641125000000, -124.1931541500000000),
(9883, 'Belfair', 115, 1, 47.4457127455000000, -122.8393221788000000),
(9884, 'Ocean Shores, Washington State', 115, 1, 47.0011138750000000, -124.1617619625000000),
(9885, 'Sequim', 115, 1, 48.0798817202000000, -123.1134475762000000),
(9886, 'Forks', 115, 1, 47.9484533077000000, -124.3832003769000000),
(9887, 'Hoquiam', 115, 1, 46.9775616828000000, -123.8789501793000000),
(9888, 'Clallam Bay', 115, 1, 48.2061500000000000, -124.3122166667000000),
(9889, 'Montesano', 115, 1, 46.9793449375000000, -123.6009958125000000),
(9890, 'Cosmopolis', 115, 1, 46.9024591200000000, -123.6992394000000000),
(9891, 'Grayland', 115, 1, 46.8008666667000000, -124.0913000000000000),
(9892, 'Port Townsend', 115, 1, 48.1107428625000000, -122.7673941656000000),
(9893, 'Port Angeles', 115, 1, 48.1135308289000000, -123.4239678488000000),
(9894, 'Neah Bay', 115, 1, 48.3673300600000000, -124.6203047200000000),
(9895, 'Moclips', 115, 1, 47.2165155000000000, -124.2051870000000000),
(9896, 'Quinault', 115, 1, 47.4708911500000000, -123.8397238000000000),
(9897, 'Port Hadlock-Irondale', 115, 1, 48.0313329000000000, -122.7625971500000000),
(9898, 'La Push', 115, 1, 47.9500500000000000, -124.3854090000000000),
(9899, 'Port Hadlock', 115, 1, 48.0342233615000000, -122.7663317077000000),
(9900, 'Aberdeen, Washington State', 115, 1, 46.9729284679000000, -123.8169967155000000),
(9901, 'Amanda Park', 115, 1, 47.4522544400000000, -123.8850234000000000),
(9902, 'Port Ludlow', 115, 1, 47.9129995100000000, -122.6861944300000000),
(9903, 'Gardiner, Washington State', 115, 1, 48.0500680000000000, -122.9230020000000000),
(9904, 'Quilcene', 115, 1, 47.8211870000000000, -122.8849048333000000),
(9905, 'Chimacum', 115, 1, 48.0041333400000000, -122.7699499200000000),
(9906, 'Brinnon', 115, 1, 47.6812000000000000, -122.9204666667000000),
(9907, 'Westport, Washington', 115, 1, 46.8997775867000000, -124.1116194300000000),
(9908, 'Kelso, Washington State', 115, 1, 46.1453348439000000, -122.9070994879000000),
(9909, 'South Bend, Washington', 115, 1, 46.6662830800000000, -123.8085672400000000),
(9910, 'Crystal Mountain', 115, 1, 46.9406263333000000, -121.4730173333000000),
(9911, 'Skamokawa', 115, 1, 46.2780526667000000, -123.4614983333000000),
(9912, 'Raymond, Washington State', 115, 1, 46.6830265857000000, -123.7246036476000000),
(9913, 'Ocean Park', 115, 1, 46.4897728611000000, -124.0491934611000000),
(9914, 'Grays River', 115, 1, 46.3585000000000000, -123.5648000000000000),
(9915, 'Elbe', 115, 1, 46.7651413200000000, -122.1939526800000000),
(9916, 'Vader', 115, 1, 46.4019970000000000, -122.9672586667000000),
(9917, 'Ryderwood', 115, 1, 46.3729690000000000, -123.0434770000000000),
(9918, 'Eatonville', 115, 1, 46.8839785588000000, -122.2813156000000000),
(9919, 'Cathlamet', 115, 1, 46.2020532357000000, -123.3816244857000000),
(9920, 'Winlock', 115, 1, 46.4905718500000000, -122.9352036500000000),
(9921, 'Kalama', 115, 1, 46.0088366000000000, -122.8443496000000000),
(9922, 'Carson, Washington State', 115, 1, 45.7441846286000000, -121.8335726857000000),
(9923, 'Naselle', 115, 1, 46.3697000000000000, -123.7919400000000000),
(9924, 'Castle Rock', 115, 1, 46.2847643931000000, -122.9019640138000000),
(9925, 'Toledo, Washington State', 115, 1, 46.4315230000000000, -122.8613820769000000),
(9926, 'Napavine', 115, 1, 46.5746266600000000, -122.9095656000000000),
(9927, 'Randle', 115, 1, 46.5407666667000000, -121.8455500000000000),
(9928, 'Tokeland', 115, 1, 46.7169000000000000, -124.0050500000000000),
(9929, 'Silver Creek, Washington State', 115, 1, 46.5222800000000000, -122.5888720000000000),
(9930, 'Skamania', 115, 1, 45.6144745000000000, -122.0525493000000000),
(9931, 'Mossyrock', 115, 1, 46.5017930300000000, -122.4799970000000000),
(9932, 'Morton, Washington State', 115, 1, 46.5568942500000000, -122.2739796000000000),
(9933, 'Toutle', 115, 1, 46.3310840000000000, -122.5415440000000000),
(9934, 'Pe Ell', 115, 1, 46.5412666667000000, -123.2884000000000000),
(9935, 'Seaview', 115, 1, 46.3335433900000000, -124.0542461000000000),
(9936, 'Ashford, Washington State', 115, 1, 46.7519000000000000, -121.9559200000000000),
(9937, 'Packwood', 115, 1, 46.6166564667000000, -121.6674312556000000),
(9938, 'Long Beach', 115, 1, 46.3529750102000000, -124.0545137878000000),
(9939, 'Stevenson, Washington State', 115, 1, 45.6938899125000000, -121.8837104417000000),
(9940, 'Ilwaco', 115, 1, 46.3071815714000000, -124.0415567143000000),
(9941, 'Onalaska, Washington State', 115, 1, 46.5793577000000000, -122.7276228000000000),
(9942, 'Chinook, Washington State', 115, 1, 46.2726843250000000, -123.9450394750000000),
(9943, 'Longview, Washington State', 115, 1, 46.1390239038000000, -122.9416697202000000),
(9944, 'Sprague', 115, 1, 47.2808507000000000, -118.0263783800000000),
(9945, 'Vantage', 115, 1, 46.9439663000000000, -119.9894423000000000),
(9946, 'Cle Elum', 115, 1, 47.1945847477000000, -120.9388687773000000),
(9947, 'Snoqualmie Pass', 115, 1, 47.4118296200000000, -121.4123030800000000),
(9948, 'Roslyn', 115, 1, 47.2235985818000000, -120.9929092182000000),
(9949, 'Ellensburg', 115, 1, 46.9932529235000000, -120.5470218200000000),
(9950, 'Easton, Washington State', 115, 1, 47.2405593600000000, -121.1799849000000000),
(9951, 'Ritzville', 115, 1, 47.1235653150000000, -118.3735922650000000),
(9952, 'North Bend, Washington', 115, 1, 47.4452781000000000, -121.4261785000000000),
(9953, 'Moses Lake', 115, 1, 47.1264047858000000, -119.2797093132000000),
(9954, 'South Cle Elum', 115, 1, 47.1840554000000000, -120.9540471000000000),
(9955, 'Kittitas', 115, 1, 46.9834140667000000, -120.4173019333000000),
(9956, 'Walla Walla', 115, 1, 46.0673544832000000, -118.3341422248000000),
(9957, 'Sunnyside', 115, 1, 46.3210742338000000, -119.9990146231000000),
(9958, 'Goldendale', 115, 1, 45.8158292458000000, -120.8188353667000000),
(9959, 'Warden', 115, 1, 46.9881200000000000, -119.0517800000000000),
(9960, 'Lowden', 115, 1, 46.0563706000000000, -118.5837323000000000),
(9961, 'Waitsburg', 115, 1, 46.2705092125000000, -118.1528192625000000),
(9962, 'Royal City', 115, 1, 46.8996368200000000, -119.6462696400000000),
(9963, 'Underwood, Washington State', 115, 1, 45.7411530000000000, -121.5546470000000000),
(9964, 'Prosser', 115, 1, 46.2125397250000000, -119.7759097917000000),
(9965, 'Mesa', 115, 1, 46.5878000000000000, -119.1852333333000000),
(9966, 'Grandview, Washington State', 115, 1, 46.2573769231000000, -119.9065538462000000),
(9967, 'Lyle', 115, 1, 45.6928965000000000, -121.2848980000000000),
(9968, 'Trout Lake', 115, 1, 45.9965945953000000, -121.5285411100000000),
(9969, 'Touchet', 115, 1, 46.0572340000000000, -118.6884843333000000),
(9970, 'Dayton, Washington State', 115, 1, 46.3193934111000000, -117.9809953056000000),
(9971, 'White Salmon', 115, 1, 45.7312393500000000, -121.4852759500000000),
(9972, 'College Place', 115, 1, 46.0448505833000000, -118.3875333000000000),
(9973, 'Bingen', 115, 1, 45.7158358600000000, -121.4686755400000000),
(9974, 'Bickleton', 115, 1, 45.9979000000000000, -120.3024000000000000),
(9975, 'Mattawa, Washington State', 115, 1, 46.7089899375000000, -119.8902536250000000),
(9976, 'Lacrosse', 115, 1, 46.8150000000000000, -117.8801500000000000),
(9977, 'Othello', 115, 1, 46.8220071800000000, -119.1685234200000000),
(9978, 'Connell', 115, 1, 46.6609100000000000, -118.8612500000000000),
(9979, 'Mabton', 115, 1, 46.2122000000000000, -119.9993000000000000),
(9980, 'Klickitat', 115, 1, 45.8171379000000000, -121.1519066000000000),
(9981, 'West Richland', 115, 1, 46.2886735474000000, -119.3449776368000000),
(9982, 'Plymouth, Washington State', 115, 1, 46.2054283000000000, -119.0884604000000000),
(9983, 'Richland, Washington State', 115, 1, 46.2719705588000000, -119.2751033930000000),
(9984, 'Highland, Washington State', 115, 1, 46.1561308000000000, -119.0779964000000000),
(9985, 'Pasco', 115, 1, 46.2487269236000000, -119.1306812579000000),
(9986, 'Kennewick', 115, 1, 46.2121488621000000, -119.1816314321000000),
(9987, 'Benton City', 115, 1, 46.2630752727000000, -119.4864219091000000),
(9988, 'Clarkston', 115, 1, 46.4141059830000000, -117.0491355149000000),
(9989, 'Uniontown, Washington State', 115, 1, 46.5145750000000000, -117.1125750000000000),
(9990, 'Pullman', 115, 1, 46.7287798835000000, -117.1751461824000000),
(9991, 'Colfax, Washington State', 115, 1, 46.8828810158000000, -117.3645618158000000),
(9992, 'Rosalia', 115, 1, 47.2379948600000000, -117.3756686000000000),
(9993, 'Pomeroy, Washington State', 115, 1, 46.4740000000000000, -117.5920666667000000),
(9994, 'Asotin', 115, 1, 46.2557102333000000, -117.0308171000000000),
(9995, 'Tekoa', 115, 1, 47.2247581000000000, -117.0730048750000000),
(9996, 'Grand Coulee', 115, 1, 47.9409455364000000, -119.0032220182000000),
(9997, 'Omak', 115, 1, 48.4137784828000000, -119.5222846103000000),
(9998, 'Cashmere', 115, 1, 47.5215183424000000, -120.4682148333000000),
(9999, 'Okanogan', 115, 1, 48.3639440800000000, -119.5812234300000000),
(10000, 'Odessa, Washington State', 115, 1, 47.3334400000000000, -118.6920800000000000),
(10001, 'Electric City', 115, 1, 47.9330761200000000, -119.0365525000000000),
(10002, 'Chelan', 115, 1, 47.8437564145000000, -120.0347214673000000),
(10003, 'Lake Wenatchee', 115, 1, 47.7853536667000000, -120.7111568500000000),
(10004, 'Dryden, Washington State', 115, 1, 47.5413740000000000, -120.5601870000000000),
(10005, 'Wilbur', 115, 1, 47.7510752000000000, -118.7031594750000000),
(10006, 'Waterville, Washington State', 115, 1, 47.6506707000000000, -120.0087710714000000),
(10007, 'Mazama', 115, 1, 48.5962100000000000, -120.4396620000000000),
(10008, 'Bridgeport, Washington State', 115, 1, 48.0084250000000000, -119.6730500000000000),
(10009, 'Davenport, Washington State', 115, 1, 47.6983855600000000, -118.1763611867000000),
(10010, 'Brewster', 115, 1, 48.1063074600000000, -119.7832786900000000),
(10011, 'Quincy, Washington State', 115, 1, 47.2086486655000000, -119.8592882034000000),
(10012, 'Twisp', 115, 1, 48.3649130048000000, -120.1276562190000000),
(10013, 'Skykomish', 115, 1, 47.7358137500000000, -121.1572932500000000),
(10014, 'Leavenworth, Washington State', 115, 1, 47.5939773316000000, -120.6624222291000000),
(10015, 'Winthrop, Washington State', 115, 1, 48.4822408308000000, -120.1941079538000000),
(10016, 'Soap Lake', 115, 1, 47.3882659375000000, -119.4839100750000000),
(10017, 'Creston, Washington State', 115, 1, 47.7586666667000000, -118.5191666667000000),
(10018, 'Tonasket', 115, 1, 48.6924812500000000, -119.4495236250000000),
(10019, 'East Wenatchee', 115, 1, 47.4086357246000000, -120.2862013462000000),
(10020, 'Coulee Dam', 115, 1, 47.9672500000000000, -118.9790500000000000),
(10021, 'Manson, Washington State', 115, 1, 47.8849878000000000, -120.1578281737000000),
(10022, 'Peshastin', 115, 1, 47.5643469250000000, -120.5989651000000000),
(10023, 'Pateros', 115, 1, 48.0536489400000000, -119.8998445858000000),
(10024, 'Ronald', 115, 1, 47.2369966000000000, -121.0255012000000000),
(10025, 'Coulee City', 115, 1, 47.6164396396000000, -119.3040583761000000),
(10026, 'Ephrata', 115, 1, 47.3168160862000000, -119.5514348448000000),
(10027, 'Oroville', 115, 1, 48.9399246842000000, -119.4322384211000000),
(10028, 'Entiat', 115, 1, 47.6798713333000000, -120.2078616667000000),
(10029, 'Wenatchee', 115, 1, 47.4327971555000000, -120.3187759784000000),
(10030, 'Conconully', 115, 1, 48.5584500000000000, -119.7502750000000000),
(10031, 'Stehekin', 115, 1, 48.3409616667000000, -120.7093353333000000),
(10032, 'Colville', 115, 1, 48.5437704583000000, -117.9084132333000000),
(10033, 'Hunters', 115, 1, 48.0920500000000000, -118.2033000000000000),
(10034, 'Valley, Washington State', 115, 1, 48.1771946500000000, -117.7399664250000000),
(10035, 'Chewelah', 115, 1, 48.2775174318000000, -117.7174104591000000),
(10036, 'Northport, Washington', 115, 1, 48.9165492400000000, -117.7808305200000000),
(10037, 'Newport, Washington State', 115, 1, 48.1704341188000000, -117.0723356250000000),
(10038, 'Usk', 115, 1, 48.3083500000000000, -117.2844000000000000),
(10039, 'Republic', 115, 1, 48.6565614118000000, -118.7134211765000000),
(10040, 'Loon Lake', 115, 1, 48.0613774000000000, -117.6273812250000000),
(10041, 'Orient, Washington State', 115, 1, 48.8888500000000000, -118.2049000000000000),
(10042, 'Curlew', 115, 1, 48.8812630500000000, -118.6029516000000000),
(10043, 'Metaline Falls', 115, 1, 48.8621847500000000, -117.3705869500000000),
(10044, 'Addy', 115, 1, 48.3939333333000000, -117.8466666667000000),
(10045, 'Kettle Falls', 115, 1, 48.6114913188000000, -118.0636226125000000),
(10046, 'Springdale, Washington State', 115, 1, 48.0207254000000000, -117.8350539667000000),
(10047, 'Coupeville', 115, 1, 48.2189563667000000, -122.6881468625000000),
(10048, 'Oak Harbor', 115, 1, 48.2967993896000000, -122.6513086583000000),
(10049, 'Langley', 115, 1, 48.0308994400000000, -122.4172888000000000),
(10050, 'Freeland', 115, 1, 48.0096490909000000, -122.5208098636000000),
(10051, 'Clinton, Washington State', 115, 1, 47.9760828000000000, -122.3766846650000000),
(10052, 'Greenbank', 115, 1, 48.0850046143000000, -122.5682237286000000),
(10053, 'NAS Whidbey Island', 115, 1, 48.3128660500000000, -122.6510395500000000),
(10650, 'Vancouver', 115, 1, 45.6448311854000000, -122.5916363861000000),
(10659, 'Bellevue', 115, 1, 47.6106708137000000, -122.1733496447000000),
(10660, 'Bothell', 115, 1, 47.7893545096000000, -122.2099924156000000),
(10661, 'Issaquah', 115, 1, 47.5431037561000000, -122.0397785298000000),
(10662, 'Kenmore', 115, 1, 47.7582871065000000, -122.2489197194000000),
(10663, 'Kirkland', 115, 1, 47.6898706583000000, -122.1960613586000000),
(10664, 'Mercer Island', 115, 1, 47.5804125040000000, -122.2338712740000000),
(10665, 'Newcastle', 115, 1, 47.5389954929000000, -122.1659221500000000),
(10666, 'Redmond', 115, 1, 47.6649031535000000, -122.1248492587000000),
(10667, 'Sammamish', 115, 1, 47.6057533041000000, -122.0343758796000000),
(10668, 'Woodinville', 115, 1, 47.7507226897000000, -122.1530125629000000),
(10669, 'Edmonds', 115, 1, 47.7992268098000000, -122.3589329287000000),
(10670, 'Lake Forest Park', 115, 1, 47.7499690154000000, -122.3002199831000000),
(10671, 'Lynnwood', 115, 1, 47.8336321883000000, -122.2889184302000000),
(10672, 'Mill Creek', 115, 1, 47.8603546084000000, -122.2105012474000000),
(10673, 'Mountlake Terrace', 115, 1, 47.7924601552000000, -122.3055110621000000),
(10674, 'Shoreline', 115, 1, 47.7524482626000000, -122.3501139598000000),
(10675, 'Everett', 115, 1, 47.9364839296000000, -122.2194170000000000),
(10676, 'Lake Stevens', 115, 1, 48.0049483672000000, -122.0916714821000000),
(10677, 'Marysville', 115, 1, 48.0819826191000000, -122.1783140185000000),
(10678, 'Mukilteo', 115, 1, 47.9099299953000000, -122.2956188576000000),
(10679, 'Snohomish', 115, 1, 47.9031816240000000, -122.1008280727000000),
(10680, 'Bainbridge Island', 115, 1, 47.6261150054000000, -122.5227373011000000),
(10681, 'Bremerton', 115, 1, 47.5826520913000000, -122.6408777496000000),
(10682, 'Gig Harbor', 115, 1, 47.3264623411000000, -122.5976950028000000),
(10683, 'Kingston', 115, 1, 47.8023000095000000, -122.5112887262000000),
(10684, 'Port Orchard', 115, 1, 47.5275809500000000, -122.6285970419000000),
(10685, 'Poulsbo', 115, 1, 47.7416695313000000, -122.6415758425000000),
(10686, 'Silverdale', 115, 1, 47.6539640367000000, -122.6905626808000000),
(10687, 'Vashon', 115, 1, 47.4448774463000000, -122.4605802537000000),
(10688, 'Bonney Lake', 115, 1, 47.1692087649000000, -122.1574540622000000),
(10689, 'Buckley', 115, 1, 47.1544640880000000, -122.0347952640000000),
(10690, 'Fife', 115, 1, 47.2412488370000000, -122.3635000761000000),
(10691, 'Graham', 115, 1, 47.0459698043000000, -122.2975497217000000),
(10692, 'Lakewood', 115, 1, 47.1641744074000000, -122.5096486262000000),
(10693, 'Milton', 115, 1, 47.2480550385000000, -122.2963364269000000),
(10694, 'Orting', 115, 1, 47.0982167500000000, -122.2065099273000000),
(10695, 'Puyallup', 115, 1, 47.1560889053000000, -122.3008518788000000),
(10696, 'Spanaway', 115, 1, 47.0857704357000000, -122.4250762310000000),
(10697, 'Steilacoom', 115, 1, 47.1724177600000000, -122.5966824800000000),
(10698, 'Sumner', 115, 1, 47.2040660230000000, -122.2330405967000000),
(10699, 'Tacoma', 115, 1, 47.2260103516000000, -122.4646076722000000),
(10700, 'Auburn', 115, 1, 47.3037147006000000, -122.2215409867000000),
(10701, 'Black Diamond', 115, 1, 47.3177017909000000, -122.0110657909000000),
(10702, 'Burien', 115, 1, 47.4666298505000000, -122.3391122608000000),
(10703, 'Covington', 115, 1, 47.3585835600000000, -122.1123818982000000),
(10704, 'Des Moines', 115, 1, 47.4036020643000000, -122.3220047500000000),
(10705, 'Enumclaw', 115, 1, 47.2021587643000000, -121.9861466500000000),
(10706, 'Federal Way', 115, 1, 47.3114564284000000, -122.3213207554000000),
(10707, 'Kent', 115, 1, 47.3911097819000000, -122.2268391399000000),
(10708, 'Maple Valley', 115, 1, 47.3757092200000000, -122.0347887673000000),
(10709, 'Pacific', 115, 1, 47.2562143583000000, -122.2516171083000000),
(10710, 'Renton', 115, 1, 47.4773051903000000, -122.1939549430000000),
(10711, 'Seatac', 115, 1, 47.4381823068000000, -122.2973077576000000),
(10712, 'Tukwila', 115, 1, 47.4622155490000000, -122.2632921686000000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
