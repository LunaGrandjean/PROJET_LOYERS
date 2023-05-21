#!/bin/bash

# Créer un nouvel environnement virtuel Conda
conda create -n myenv python=3.8 -y

# Activer l'environnement virtuel
source activate myenv

# Installer les bibliothèques nécessaires
conda install -c anaconda pandas -y
conda install -c anaconda chardet -y
conda install -c conda-forge pandas-profiling -y
conda install -c anaconda glob2 -y
conda install -c conda-forge matplotlib -y
conda install -c anaconda seaborn -y
conda install -c plotly plotly -y

# Afficher un message indiquant que l'installation est terminée
echo "L'environnement virtuel a été créé et les bibliothèques ont été installées."
