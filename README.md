Overall project goal: To provide access to images in archives with their date of capture, and thier geographic location. A later adaptation of the project would include incorporating this data in a mapping layer in the interest of tracking how locations change throughout history.

Le bût principal de ce projet serait de créer une base de donnés d'images historiques pour finalement
associer les dates et la geolocalisation avec chaque image. Cela dans le bût de fournir des données pour un
projet avec un système cartographique (e.g. un plugin google maps) pour montrer aux utilisateurs comment le
paysage urbain et naturel aurait changé au fil des années. 

Project documentation:


    image_scraper.py

    Ce dossier sert comme la plaque fondatrice pour une évolution vers des applications qui s'en serviront
    pour faire des recherches d'images sur un grand plan. Le code sera incorporé dans une classe python qui
    sera invoquée par d'autres scriptes.

    This file serves as the base file for eventual scraping work. The code will be wrapped in a class
    that will be invoked by more detailed tailored scraping scripts. Most likely, specific scripts will have
    to be used for each particular website.
