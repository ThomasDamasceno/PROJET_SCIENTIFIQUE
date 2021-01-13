window.onload = function () {
  var mymap = L.map("mapid").setView([45.75, 4.85], 12); //création de la map avec les coordonnées de l'agglo de Lyon
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
    {
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: "mapbox/streets-v11",
      tileSize: 512,
      zoomOffset: -1,
      accessToken:
        "pk.eyJ1IjoiZW1pbGVhcmd0ZSIsImEiOiJja2ppYXN3YTgwMWxhMzhzN2d5N211M3I0In0.MoGt06oEn_yTUOmdfIa_aA", //token de connexion à Mapbox
    }
  ).addTo(mymap);

  var cercle = []; //variable pour stocker les cercles (feux)
  var camions_liste = []; // variable pour stocker les camions

  unload();
  function unload() {
    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = () => {
      // verifie si transaction est terminée
      if (xmlhttp.readyState == 4) {
        // on a passé les 4 etapes
        //si la transcation est un succès
        if (xmlhttp.status == 200) {
          //on traite les données recus
          console.log(xmlhttp.responseText);
          let donnees = JSON.parse(xmlhttp.responseText);

          cercle.forEach(function (marker) {
            mymap.removeLayer(marker); //supprime les cercles de la map
          });
          cercle = []; //on supprime le tableau à chaque fois

          camions_liste.forEach(function (marker) {
            mymap.removeLayer(marker); //supprimer les camions de la liste
          });
          camions_liste = []; //on supprime le tableau à chaque fois

          $("#liste_feux").empty(); //on vide la liste pour eviter les doublons
          $("#liste_camions").empty();

          console.log(donnees);
          donnees[0].feux.forEach((feu) => {
            //on boucle sur les feux
            //on boucle sur les donnees
            // on crée un cercle pour le feu
            let marker = L.circle([feu.lat, feu.lon], {
              color: "red", // couleur bordure
              fillColor: "#f03", // couleur du remplissage
              radius: feu.intensite, //on gere le diametre du cercle selon l'intensite
            }).addTo(mymap);

            cercle.push(marker); //on stocke les cercles dans le tableau cercle
            console.log(cercle);
            $("#liste_feux").prepend(
              "<div><b>Feu ID : " +
                feu.id +
                "</b> <br> Intensite : " +
                feu.intensite +
                "<br> Longitude : " +
                feu.lon +
                "<br> Latitude : " +
                feu.lat +
                "</div>"
            ); //JQUERY AFFICHER LISTE FEUX
            marker.bindPopup(
              "<b>Feu ID : " +
                feu.id +
                "</b> <br> Intensite : " +
                feu.intensite +
                "<br> Longitude : " +
                feu.lon +
                "<br> Latitude : " +
                feu.lat
            ); // popup lorsqu'on clique sur un feu
          });

          donnees[1].camions.forEach((camion) => {
            var camionIcon = L.icon({
              iconUrl: "camion.png",
              iconSize: [35, 40], // size of the icon
            });

            let marker = L.marker([camion.lat, camion.lon], {
              icon: camionIcon,
            }).addTo(mymap);

            camions_liste.push(marker);
            $("#liste_camions").prepend(
              "<div><b>Camion ID : " +
                camion.id +
                "</b> <br> Statut : " +
                camion.statut +
                "<br> Longitude : " +
                camion.lon +
                "<br> Latitude : " +
                camion.lat +
                "<br> Affecté au feu ID: " +
                camion.feu_id +
                "</div>" 
            ); //JQUERY AFFICHER LISTE CAMIONS
            marker.bindPopup(
              "<b>Camion ID : " +
                camion.id +
                "</b> <br> Statut : " +
                camion.statut +
                "<br> Longitude : " +
                camion.lon +
                "<br> Latitude : " +
                camion.lat +
                "<br> Affecté au feu ID : " +
                camion.feu_id
            ); // popup lorsqu'on clique sur un feu
          });
        } else {
          console.log(xmlhttp.statusText);
        }
      }
    };

    xmlhttp.open("GET", "http://localhost/Feu/Emergency/BACKEND/liste.php"); // requete GET depuis notre page de traitement
    xmlhttp.send(null); // on ecrit null car on envoie pas de données on recupere seulement

    setTimeout(unload, 2000); //appelle unload toutes les 1 sec
  }
};
