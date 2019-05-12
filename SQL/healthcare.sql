-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.5.0.5332
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for healthcare
CREATE DATABASE IF NOT EXISTS `healthcare` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `healthcare`;

-- Dumping structure for table healthcare.diseases
CREATE TABLE IF NOT EXISTS `diseases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table healthcare.diseases_symptoms
CREATE TABLE IF NOT EXISTS `diseases_symptoms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `diseases_id` int(11) DEFAULT NULL,
  `symptoms_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=197 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table healthcare.symptoms
CREATE TABLE IF NOT EXISTS `symptoms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `symptoms` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=143 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
