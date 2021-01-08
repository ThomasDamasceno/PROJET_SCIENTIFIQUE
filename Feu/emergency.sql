-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 08 jan. 2021 à 14:24
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
-- Base de données : `emergency`
--

-- --------------------------------------------------------

--
-- Structure de la table `camion`
--

DROP TABLE IF EXISTS `camion`;
CREATE TABLE IF NOT EXISTS `camion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  `statut` tinyint(1) NOT NULL,
  `feu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_feuid` (`feu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `camion`
--

INSERT INTO `camion` (`id`, `lat`, `lon`, `statut`, `feu_id`) VALUES
(5, 45.738, 4.812, 1, 153);

-- --------------------------------------------------------

--
-- Structure de la table `feu`
--

DROP TABLE IF EXISTS `feu`;
CREATE TABLE IF NOT EXISTS `feu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intensite` tinyint(4) UNSIGNED NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lat` (`lat`),
  UNIQUE KEY `lon` (`lon`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `feu`
--

INSERT INTO `feu` (`id`, `intensite`, `lat`, `lon`) VALUES
(153, 38, 45.739499124736554, 4.813514074753513);

-- --------------------------------------------------------

--
-- Structure de la table `pompier`
--

DROP TABLE IF EXISTS `pompier`;
CREATE TABLE IF NOT EXISTS `pompier` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `camion`
--
ALTER TABLE `camion`
  ADD CONSTRAINT `fk_feuid` FOREIGN KEY (`feu_id`) REFERENCES `feu` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
