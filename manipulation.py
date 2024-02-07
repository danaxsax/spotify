import pandas as pd
import plotly.express as px
import functions as ft
pd.options.plotting.backend = "plotly"

def cleaning_and_menu():
    pd.options.plotting.backend = "plotly"
    #cargar el csv
    df = pd.read_csv("spotify-2023.csv", encoding='latin-1')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    NaN_values = df.isna() #True donde hay valores NaN
    any_missing_values = NaN_values.any().any() #verifica si hay NaN en cualquier parte del df
    missing_value_columns = NaN_values.any() #retorna True para columnas con NaN row
    missing_value_counts = df.isnull().sum() #suma de la cantidad de registros NaN por columna
    print(f"Hay valores faltantes? {any_missing_values}\n")
    #print(f"Valores faltantes \n{missing_value_columns}\n")
    for column, has_missing in missing_value_columns.items():
        if has_missing:
            count = missing_value_columns[column]
            print(f"------> Columna '{column}' : {count}")
    print(f"\nRegistros faltantes por columna \n{missing_value_counts}")
    print("\n⋆ ˚｡⋆୨୧˚✩₊˚.⋆☾⋆⁺₊✧Magia de limpieza⋆ ˚｡⋆୨୧˚✩₊˚.⋆☾⋆⁺₊✧\n")
    #cleaning
    df_cleaned = df.dropna() #eliminas registros con NaN
    #df.info()
    
    print("＊*•̩̩͙✩•̩̩͙*˚*•̩̩͙✩•̩̩͙*˚＊⭒⭒*•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚＊⭒Hola•̩̩͙✩•̩̩͙*˚⍣˚*•̩̩͙✩•̩̩͙*˚˚⍣＊⭒˚⍣⭒＊*•̩̩͙✩•̩̩͙*˚⍣˚")
    print("1. Taylor Swift most succesfull records !")
    print("2. Caracteristicas que debería tener tu record para triunfar")
    print("3. Se relacionan los streams con las veces que se guardó en playlist?")
    print("4. Top songs basada en las veces que se guardó en playlist")
    print("5. Fechas en que más se saca musica")
    print("6. Los duos más chambeadores (artistas que colaboraron más)")
    print("7. La canción top por año")
    selected = int(input("Qué opcion quieres? "))

    dictionary = {
        1: ft.taylors_version,
        2: ft.to_the_hits,
        3: ft.streams_playlist,
        4: ft.top_playlist,
        5: ft.dates,
        6: ft.duos,
        7: ft.top_per_year
    }
    answer = 1
    while answer == 1:
        if selected in dictionary:
            return dictionary[selected](df_cleaned)
        answer = input("1. Ver menu otra vez \n2. End")
        
cleaning_and_menu()