#!/bin/bash

# Créez un nouvel environnement virtuel Conda
conda create -n myenv python=3.8

# Activez l'environnement virtuel
source $(conda info --base)/etc/profile.d/conda.sh
conda activate myenv

# Installez les bibliothèques nécessaires
conda install pandas
conda install matplotlib
conda install seaborn
conda install jupyter
conda install chardet
conda install pandas-profiling
conda install glob2

# Affichez un message indiquant que l'installation est terminée
echo "L'environnement virtuel a été créé et les bibliothèques suivantes ont été installées :"

# Affichez les bibliothèques installées en colonne
conda list | awk '{print $1}' | column
