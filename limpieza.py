import pandas as pd
import numpy as np

def limpiar_datos(df):
    # Reemplazar valores nulos o no realistas con la media de la columna correspondiente
    df['Age'] = df['Age'].apply(lambda x: x if 0 <= x <= 60 else np.nan)
    df['Salary'] = df['Salary'].apply(lambda x: x if x >= 30000 else np.nan)

    # Calcular la media de la tabla completa para Age y Salary
    media_age = df['Age'].mean()
    media_salary = df['Salary'].mean()

    # Reemplazar valores nulos por la media
    df['Age'] = df['Age'].fillna(media_age)
    df['Salary'] = df['Salary'].fillna(media_salary)

    # Reemplazar otros valores nulos en las demás columnas con la media o un valor específico
    for col in df.columns:
        if df[col].dtype != 'object':  # Para columnas numéricas
            df[col] = df[col].fillna(df[col].mean())

    return df
