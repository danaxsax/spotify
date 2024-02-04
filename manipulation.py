import pandas as pd
df = pd.read_csv("spotify-2023.csv", encoding='latin-1')
#1.- check data unique rows, unique series

def cleaning():
    if df.index.is_unique & df.columns.is_unique:
        print("unique rows and columns!")
    else:
        dup = df.duplicated()
        for index, value in dup.items():
            if value:
                print(f"The duplicated series are: {df.loc[index]}")
        df.drop_duplicates(inplace=True)

def main():
    #elimina registros duplicados
    df= df.drop_duplicates()
    
main()

        
    