<?php

// Fichier permet d'effectuer la requete

class Feu{
    // Connexion
    private $connexion;
    private $table = "feu";

    // object properties
    public $id;
    public $intensite;
    public $lat;
    public $lon;

    /**
     * Constructeur avec $db pour la connexion à la base de données
     *
     * @param $db
     */
    public function __construct($db){
        $this->connexion = $db;
    }

    /**
     * Lecture des feux
     *
     * @return object
     */
    public function lire(){
        // On écrit la requête
        $sql = "SELECT * FROM " . $this->table;

        // On prépare la requête
        $query = $this->connexion->prepare($sql);

        // On exécute la requête
        $query->execute();

        // On retourne le résultat
        return $query;
    }

    public function ecrire(){
        //on écrit la requete
        $sql = "INSERT INTO " . $this->table . " (intensite,lat,lon) VALUES (" 
            . $this->intensite . "," . $this->lat .",". $this->lon . ")";
        
        // On prépare la requête
        $query = $this->connexion->prepare($sql);

        // On exécute la requête
        $query->execute();

        // On retourne le résultat
        return $query;  
    }
}