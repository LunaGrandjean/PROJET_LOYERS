﻿Le présent projet porte sur l'analyse de données françaises fournies par les différents observatoires des loyers. Nos données incluent des métriques (moyenne, médiane, ...) sur les montants de loyers pour des échantillons de logements dans différentes agglomérations, pour différentes années, différents types d'habitations, ...

Les données traitées sont issues de la page suivante : https://www.data.gouv.fr/fr/datasets/resultats-nationaux-des-observatoires-locaux-des-loyers/#/resources 

Notre question de recherche est : quels facteurs environnementaux et socio-économiques sont liés aux différences de montants des loyers en France entre 2014 et 2022 ? Il s'agit de considérer la France en général, pas seulement la France métropolitaine.

Le code suivant a été utilisé pour créer notre environnement virtuel :

\# Créer un nouvel environnement virtuel Conda

conda create -n myenv python=3.8

\# Activer l'environnement virtuel

conda activate myenv

\# Installer les bibliothèques nécessaires

conda install pandas matplotlib seaborn jupyter

\# Afficher un message indiquant que l'installation est terminée

echo "L'environnement virtuel a été créé et les bibliothèques ont été installées."
