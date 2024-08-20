import pandas as pd

def mostrar_columnas(df):
    print("\nColumnas disponibles:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {col}")

def mostrar_datos_paginate(df, start, end):
    """
    Muestra un rango de filas del DataFrame.
    """
    print(df.iloc[start:end])

def modificar_datos(df):
    while True:
        mostrar_columnas(df)
        
        try:
            col_index = int(input("\nSelecciona el índice de la columna que deseas modificar (o -1 para salir): "))
            if col_index == -1:
                break

            if col_index < 0 or col_index >= len(df.columns):
                print("Índice no válido. Intenta de nuevo.")
                continue

            col_name = df.columns[col_index]
            print(f"Has seleccionado la columna: {col_name}")

            # Mostrar datos en secciones de 10 filas
            num_filas = len(df)
            start = 0
            end = 10
            
            while end <= num_filas:
                mostrar_datos_paginate(df, start, end)
                start += 10
                end += 10
                if end > num_filas:
                    end = num_filas
                
                if end == num_filas:
                    print(df.iloc[start:])
                
                # Esperar input del usuario para continuar
                if end < num_filas:
                    continuar = input("¿Deseas ver la siguiente sección de datos? (s/n): ").lower()
                    if continuar != 's':
                        break
            
            row_index = int(input("Selecciona el índice de la fila que deseas modificar: "))
            if row_index < 1 or row_index > len(df):
                print("Índice de fila no válido. Intenta de nuevo.")
                continue

            nuevo_valor = input(f"Ingresa el nuevo valor para la columna '{col_name}' en la fila {row_index}: ")
            
            if pd.api.types.is_numeric_dtype(df[col_name]):
                nuevo_valor = pd.to_numeric(nuevo_valor, errors='coerce')

            df.at[row_index - 1, col_name] = nuevo_valor
            print("Valor modificado exitosamente.")
            print(df[[col_name]])

        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar un número.")
        
        continuar = input("¿Quieres modificar otro valor? (s/n): ").lower()
        if continuar != 's':
            break

    return df

if __name__ == "__main__":
    archivo = 'synthetic_data_usd.csv'
    df = pd.read_csv(archivo)
    df.index = df.index + 1

    df_modificado = modificar_datos(df)

    guardar = input("¿Deseas guardar los cambios? (s/n): ").lower()
    if guardar == 's':
        nombre_archivo = input("Ingresa el nombre del archivo para guardar (con extensión .csv): ")
        df_modificado.to_csv(nombre_archivo, index=False)
        print(f"Datos guardados en {nombre_archivo}")
    else:
        print("Cambios descartados.")
