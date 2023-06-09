import pandas as pd


def get_hechos_df():
    """obtiene dataframe de transformaciones de dataset tabla_hechos"""
    return pd.read_csv('../ETL/transformations/tabla_hechos_final.csv')

def get_ith():
    """obtiene dataframe de transformaciones de dataset ith"""
    return pd.read_csv('../ETL/transformations/tabla_ith.csv')


def get_daily_distances_df():
    """obtiene dataframe de transformaciones distancias diarias"""
    return pd.read_csv('../ETL/transformations/GPS_distancia_diaria.csv')

def get_recorrido_diario_df():
    return pd.read_csv('../ETL/transformations/GPS_recorrido_individual.csv')
