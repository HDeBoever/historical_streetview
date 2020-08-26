0.0

Overall project goal: To provide access to images in archives with their date of capture, and their geographic location. A later adaptation of the project would include incorporating this data in a mapping layer in the interest of tracking how locations change throughout history. Also a testbed for me to play with Google Geographic APIs

Le but principal de ce projet de recherche serait de créer une base de donnés d'images historiques pour
finalement associer les dates et la geolocalisation avec chaque image. Cela dans le but de fournir des
données pour un projet avec un système cartographique (e.g. un plugin google maps) pour montrer aux
utilisateurs comment le paysage urbain et naturel aurait changé au fil des années. Ceçi est un projet
multidisciplinaire qui demande une compréhension de la photographie, la géographie, le codage informatique,
et un esprit de curiosité envers le patrimoine historique humain dans le but de le préserver.

En ce moment, j'envisage une interface entre des photos à partir de reddit (spécifiquement le sub
r/oldphotosinreallife) et des fichiers .kml. Les APIs de google seront utilisés pour fournir des
informations pour chaque endroit dans chaque photographe.

Use this bash script for now : https://github.com/ostrolucky/Simple-Subreddit-Image-Downloader
Usage: ./download-subreddit-images.sh <subreddit_name>

1.0 Project documentation:

    1.1 image_scraper.py

    Ce fichier firgure parmis les premières démarches vers une évolution vers des applications qui s'en
    serviront pour faire des recherches d'images sur un grand plan. Le code sera incorporé dans une classe python qui sera invoquée par d'autres scriptes.

    This file serves as the base file for eventual scraping work. The code will be wrapped in a class
    that will be invoked by more detailed tailored scraping scripts. Most likely, specific scripts will have
    to be used for each particular website.

    1.2 kml_write.py

    Pour intégrer les images sur une carte en coordonnées géographiques.

        1.2.0 get_coords(location)
        Selon une addresse ou un endroit, cette fonction rend les coordonés géographiques de l'endroit
        fourni. Cette fonction se sert de l'API google maps pour arriver à cette fonctionalité.

2.0 Dependencies/ dépendances

    Je considère l'utilisation de n'importe quel logiciel qui pourra faire une interface convenable avec des
    fichiers type .kml ou type .kmz, donc QGis, ArcGis, Google Earth, etc.

    Donc, à partir de maintenant, les API de Google seront utilisés pour créer des couches géographiques
    compatibles avec google maps et des outils géographiques. En ce moment, nous utilisons le API Google Places. La clé de cet API
    est sauvegardée localement pour le moment de façon à ne pas compromettre la sécurité de mon compte Google en question.


3.0 Dossier test_kml_files

    Ce dossier contient des fichiers téléchargeables que vous pouvez essayer sur Google Earth.

    This folder contains readily downloadable files that you can try in Google Earth. The generation of these files will depend on the computer also having the images downloaded on the local machine in order to be integrated.

4.0 Utilisation du programme / Program Usage

    image_scraper.py  --- > kml_write.py
