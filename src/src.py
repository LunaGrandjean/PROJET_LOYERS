import glob
import pandas as pd
from typing import List


def load_and_concatenate_csv_files(file_pattern: str) -> pd.DataFrame:
    """
    Charge et concatène les fichiers CSV correspondant au motif de fichier donné.
    
    :param file_pattern: str, motif du fichier à rechercher (ex: "Base_OP_*_Nationale.csv").
    :return: DataFrame, DataFrame combiné contenant toutes les données des fichiers CSV correspondants.
    """
    files = glob.glob(file_pattern)

    all_dataframes = []

    for file_name in files:
        df = pd.read_csv(file_name, encoding='ISO-8859-1', sep=';')
        all_dataframes.append(df)

    # Concaténer tous les dataframes
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    return combined_df


def combine_nombre_observations_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine les colonnes 'nombre_obsservations' et 'nombre_observations' en une seule colonne.

    :param df: pd.DataFrame, le DataFrame d'origine.
    :return: pd.DataFrame, le DataFrame avec les colonnes combinées.
    """
    if 'nombre_obsservations' in df.columns and 'nombre_observations' in df.columns:
        df['nombre_observations'] = df['nombre_observations'].fillna(0) + df['nombre_obsservations'].fillna(0)
        df.drop(columns=['nombre_obsservations'], inplace=True)
    else:
        print("One or both columns are missing.")
    return df


def clean_and_filter_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et filtre les colonnes 'anciennete_locataire_homogene' et 'epoque_construction_homogene'.

    :param df: pd.DataFrame, le DataFrame d'origine.
    :return: pd.DataFrame, le DataFrame avec les colonnes nettoyées et filtrées.
    """
    df['anciennete_locataire_homogene'] = df['anciennete_locataire_homogene'].str.replace(r'\d+\.', '',
                                                                                          regex=True).str.strip()
    df['epoque_construction_homogene'] = df['epoque_construction_homogene'].str.replace(r'\d+. ', '', regex=True)

    df["nombre_pieces_homogene"] = df["nombre_pieces_homogene"].replace(r' et plus', '+', regex=True)

    valid_values = ['Avant 1946', 'Entre 1946-1970', 'Entre 1971-1990', 'Entre 1991-2005', 'Après 2005']
    df = df[df['epoque_construction_homogene'].isin(valid_values) | df['epoque_construction_homogene'].isna()]

    return df


def clean_and_remove_other_values(df: pd.DataFrame, column: str, valid_values: List[str]) -> pd.DataFrame:
    """
    Nettoie et supprime les lignes avec des valeurs autres que celles spécifiées dans 'valid_values'
    pour la colonne spécifiée.

    :param df: pd.DataFrame, le DataFrame d'origine.
    :param column: str, le nom de la colonne à nettoyer et filtrer.
    :param valid_values: List[str], une liste de valeurs valides pour la colonne spécifiée.
    :return: pd.DataFrame, le DataFrame avec la colonne nettoyée et les lignes non valides supprimées.
    """
    df_copy = df.copy()
    df_copy[column] = df_copy[column].str.replace(r'\d+\.', '', regex=True).str.strip()
    df_copy = df_copy[df_copy[column].isin(valid_values)]

    return df_copy


def process_grouped_data(df: pd.DataFrame, excluded_value: str, groupby_column: str, value_column: str) -> pd.DataFrame:
    """
    Traite les données groupées en excluant une valeur spécifique, en calculant la moyenne et l'écart-type
    des données et en triant les résultats par la moyenne.

    :param df: pd.DataFrame, le DataFrame d'origine.
    :param excluded_value: str, la valeur à exclure du DataFrame.
    :param groupby_column: str, le nom de la colonne sur laquelle effectuer le groupby.
    :param value_column: str, le nom de la colonne dont on calcule la moyenne et l'écart-type.
    :return: pd.DataFrame, le DataFrame fusionné et trié par la moyenne.
    """
    filtered_df = df[df[groupby_column] != excluded_value]
    grouped_mean = filtered_df.groupby(groupby_column)[value_column].mean().reset_index()
    grouped_std = filtered_df.groupby(groupby_column)[value_column].agg(lambda x: x.dropna().std()).reset_index()
    grouped = pd.merge(grouped_mean, grouped_std, on=groupby_column, suffixes=('_mean', '_std'))
    grouped = grouped.sort_values(by=f'{value_column}_mean')

    # Filter out rows with NaN values in the '_std' column
    grouped = grouped.dropna(subset=[f'{value_column}_std'])

    return grouped


def load_and_process_complementary_dataframe(file_path: str) -> pd.DataFrame:
    """
    Charge et traite le DataFrame complémentaire en renommant certaines colonnes.

    :param file_path: str, chemin du fichier CSV à charger.
    :return: pd.DataFrame, le DataFrame complémentaire traité.
    """
    df_complementary = pd.read_csv(file_path, sep=';')
    df_complementary.rename(columns={"TMin (°C)": "TMin", "TMax (°C)": "TMax", "TMoy (°C)": "TMoy"}, inplace=True)

    return df_complementary


def select_departments(df: pd.DataFrame, department_codes: List[str]) -> pd.DataFrame:
    """
    Sélectionne les lignes d'un DataFrame en fonction des codes de département.

    :param df: pd.DataFrame, le DataFrame à filtrer.
    :param department_codes: List[str], une liste de codes de département à sélectionner.
    :return: pd.DataFrame, un nouveau DataFrame contenant uniquement les lignes avec les codes de département sélectionnés.
    """
    df_selection = df[df['Code INSEE département'].isin(department_codes)]

    return df_selection
