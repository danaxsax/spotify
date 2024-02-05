import pandas as pd
#cargar el csv
df = pd.read_csv("spotify-2023.csv", encoding='latin-1')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

NaN_values = df.isna() #True donde hay valores NaN
any_missing_values = NaN_values.any().any() #verifica si hay NaN en cualquier parte del df
missing_value_columns = NaN_values.any() #retorna True para columnas con NaN row
missing_value_counts = df.isnull().sum() #suma de la cantidad de registros NaN por columna

#outputs
print(f"Hay valores faltantes? {any_missing_values}\n")
print(f"Valores faltantes \n{missing_value_columns}\n")
for column, has_missing in missing_value_columns.items():
    if has_missing:
        count = missing_value_columns[column]
        print(f"------> Columna '{column}' : {count}")
print(f"\nRegistros faltantes por columna \n{missing_value_counts}")

#cleaning
df.dropna(subset=["key"], inplace=True) #eliminas registros con NaN
df.info()

