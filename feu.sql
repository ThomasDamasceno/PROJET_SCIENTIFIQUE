-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 05 jan. 2021 à 15:46
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `feu`
--

-- --------------------------------------------------------

--
-- Structure de la table `feu`
--

DROP TABLE IF EXISTS `feu`;
CREATE TABLE IF NOT EXISTS `feu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intensite` int(11) NOT NULL,
  `lat` decimal(10,8) NOT NULL,
  `lon` decimal(10,8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lat` (`lat`),
  UNIQUE KEY `lon` (`lon`)
) ENGINE=MyISAM AUTO_INCREMENT=60 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `feu`
--

INSERT INTO `feu` (`id`, `intensite`, `lat`, `lon`) VALUES
(1, 50, '45.74500000', '4.82000000'),
(2, 210, '45.74200000', '4.89000000'),
(3, 15, '45.74800000', '4.85700000'),
(4, 255, '45.74100000', '4.85200000'),
(5, 40, '45.76933000', '4.85503000'),
(46, 37, '45.74462690', '4.84422511'),
(47, 18, '45.76200993', '4.88930954'),
(48, 25, '45.72615823', '4.87785043'),
(49, 43, '45.76829747', '4.89103924'),
(50, 46, '45.76554799', '4.85210898'),
(51, 15, '45.74709723', '4.82253483'),
(52, 3, '45.74473295', '4.88088243'),
(53, 30, '45.78295201', '4.86779815'),
(54, 29, '45.77867489', '4.79145324'),
(55, 26, '45.74098123', '4.83538129'),
(56, 47, '45.77079401', '4.81565734'),
(57, 23, '45.75892363', '4.84888301'),
(58, 16, '45.74898322', '4.84366337'),
(59, 11, '45.72851899', '4.83236573');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
