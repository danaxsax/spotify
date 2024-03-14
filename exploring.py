import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"

df = pd.read_csv("spotify-2023.csv", encoding='latin1')

pd.set_option('display.max_rows', None)    
pd.set_option('display.max_columns', None)
print(df.info())
#print(df.dtypes)
#print(df.head())
df.dropna()
#print(df.head(10))
coma = ","
colabs = df["artist(s)_name"].str.find(coma)
print(colabs.head(10))
