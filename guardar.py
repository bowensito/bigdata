import pandas as pd

def guardar_datos(df, nombre_archivo='datos_limpiados.csv'):
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en {nombre_archivo}")
