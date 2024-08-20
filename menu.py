import pandas as pd
from limpieza import limpiar_datos
from guardar import guardar_datos

archivo = 'synthetic_data_usd.csv'
df = pd.read_csv(archivo)

def mostrar_seccion(df, start, end):
    print(df.iloc[start:end])

def menu():
    pd.set_option('display.max_rows', 10)
    df_limpio = None
    start = 0 
    step = 10

    while True:
        print("\nOpciones del Menú:")
        print("1. Limpiar los datos")
        print("2. Guardar los datos limpios")
        print("3. Visualizar tabla completa de datos limpios")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            df_limpio = limpiar_datos(df)
            df_limpio.index = df_limpio.index + 1
            print("Datos limpiados correctamente.")
        elif opcion == '2':
            if df_limpio is not None:
                nombre_archivo = input("Ingresa el nombre del archivo para guardar (con extensión .csv): ")
                guardar_datos(df_limpio, nombre_archivo)
            else:
                print("Primero debes limpiar los datos.")
        elif opcion == '3':
            if df_limpio is not None:
                while True:
                    mostrar_seccion(df_limpio, start, start + step)
                    accion = input("\nNavegar: 'd' (siguiente), 'a' (anterior), 'q' (salir): ").lower()
                    
                    if accion == 'd':
                        if start + step < len(df_limpio):
                            start += step
                        else:
                            print("Has llegado al final de la tabla.")
                    elif accion == 'a':
                        if start - step >= 0:
                            start -= step
                        else:
                            print("Estás en el inicio de la tabla.")
                    elif accion == 'q':
                        break
                    else:
                        print("Opción no válida.")
            else:
                print("Primero debes limpiar los datos.")
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
