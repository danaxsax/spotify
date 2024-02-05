def importNreading():
    import pandas as pd
    df = pd.read_csv("spotify-2023.csv", encoding='latin-1')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    
def cleaning():
    #elimina registros duplicados
    df = df.drop_duplicates()
    #verifica para cada columna si hay un NaN, si si lo reemplaza con 0
    for column in df:
        df[column] = df[column].fillna("0")
    #elimina registros donde no hay key
    df = df.dropna(subset=['key'])

importNreading()
cleaning()

        
    