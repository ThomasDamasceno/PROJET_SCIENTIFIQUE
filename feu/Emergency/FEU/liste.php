<?php
//FICHIER CONTIENT LE TRAITEMENT DE LA DEMANDE

// Headers requis
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: GET");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// On vérifie que la méthode utilisée est correcte
if($_SERVER['REQUEST_METHOD'] == 'GET'){
    // On inclut les fichiers de configuration et d'accès aux données
    include_once './database.php';
    include_once './feu.php';

    // On instancie la base de données
    $database = new Database();
    $db = $database->getConnection();

    // On instancie les feux
    $feu = new Feu($db);

    //On instancie les camions
    $camion = new Camion($db);

    // On récupère les données des feux
    $stmt = $feu->lire();

    //On récupère les données des camions
    $stmg = $camion->lire();

    // Lancement du traitement
    if($stmt->rowCount() >= 0){
        // On initialise un tableau associatif
        $tableauFeux = [];
        $tableauFeux['feux'] = [];

        $tableauCamions = [];
        $tableauCamions['camions'] = [];

        // On parcourt les feux
        while($row = $stmt->fetch(PDO::FETCH_ASSOC)){
            extract($row);

            $feufeu = [
                "id" => $id,
                "intensite" => $intensite,
                "lat" => $lat,
                "lon" => $lon,
            ];

            $tableauFeux['feux'][] = $feufeu;
        }

        //On parcourt les camions
        while($row = $stmg->fetch(PDO::FETCH_ASSOC)){
            extract($row);

            $camcam = [
                "id" => $id,
                "lat" => $lat,
                "lon" => $lon,
                "statut" => $statut,
                "feu_id" => $feu_id
            ];

            $tableauCamions['camions'][] = $camcam;
        }

        // On envoie le code réponse 200 OK
        http_response_code(200);

        // On encode en json et on envoie
        echo json_encode([$tableauFeux,$tableauCamions]);
    }

}else{
    // On gère l'erreur
    http_response_code(405);
    echo json_encode(["message" => "La méthode n'est pas autorisée"]);
}