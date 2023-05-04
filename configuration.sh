# Créer un nouvel environnement virtuel Conda
conda create -n myenv python=3.8

# Activer l'environnement virtuel
conda activate myenv

# Installer les bibliothèques nécessaires
conda install pandas=2.0.1 ydata_profiling=4.1.2 glob=3.11.3

# Afficher un message indiquant que l'installation est terminée
echo "L'environnement virtuel a été créé et les bibliothèques ont été installées."
