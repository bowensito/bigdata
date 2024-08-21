import pandas as pd
import matplotlib.pyplot as plt

def analisis_descriptivo(df):
    print("\nEstadísticas descriptivas básicas:\n")
    print(df.describe(include='all'))

    print("\nConteo de valores nulos por columna:\n")
    print(df.isnull().sum())

    print("\nCorrelaciones entre variables numéricas:\n")
    print(df.corr())

    cols_categoricas = df.select_dtypes(include=['object']).columns
    for col in cols_categoricas:
        print(f"\nFrecuencia de valores únicos en '{col}':\n")
        print(df[col].value_counts())

    df.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 6))
    correlaciones = df.corr()
    plt.matshow(correlaciones, cmap='coolwarm', fignum=1)
    plt.colorbar()
    plt.title("Matriz de Correlación", pad=15)
    plt.xticks(range(len(correlaciones.columns)), correlaciones.columns, rotation=45, ha="left")
    plt.yticks(range(len(correlaciones.columns)), correlaciones.columns)
    plt.show()
