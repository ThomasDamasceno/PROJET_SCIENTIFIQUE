<?php

//FICHIER CONTIENT LE TRAITEMENT DE LA DEMANDE

// Headers requis
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// On vérifie que la méthode utilisée est correcte
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // On inclut les fichiers de configuration et d'accès aux données
    include_once './database.php';
    include_once './feu.php';

    // On instancie la base de données
    $database = new Database();
    $db = $database->getConnection();

    $content = file_get_contents('php://input');

    

    if (($elem = json_decode($content, true) != null)) {

        $feu = new Feu($db);
        $feu->statut = 1;
        $feu->lon = round ($elem['lo'], 7);
        $feu->lat = round ($elem['la'], 6);
        
        $FILE = fopen('eteindre.txt','w');
        fwrite($FILE, $feu->lat . "," . $feu->lon);

        $feu->eteindre(); 
      

        // On envoie le code réponse 200 OK
        http_response_code(200);
    }
} else {
    // On gère l'erreur
    http_response_code(405);
    echo json_encode(["message" => "La méthode n'est pas autorisée"]);
}
