#!/bin/bash

# Créez un nouvel environnement virtuel Conda
conda create -n myenv python=3.8

# Activez l'environnement virtuel
conda activate myenv

# Installez les bibliothèques nécessaires
conda install pandas matplotlib seaborn jupyter chardet pandas_profiling glob

# Affichez un message indiquant que l'installation est terminée
echo "L'environnement virtuel a été créé et les bibliothèques ont été installées."
