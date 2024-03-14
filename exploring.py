import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"

df = pd.read_csv("database/spotify-2023.csv", encoding='latin1')

pd.set_option('display.max_rows', None)    
pd.set_option('display.max_columns', None)
print(df.info())
#print(df.dtypes)
#print(df.head())
df.dropna()
#print(df.head(10))
a = df.sort_values(by = "artist_count", ascending=False).head(10)
print(a["artist_count"])

a[['artist_1', 'artist_2', 'artist_3', 'artist_4', 'artist_5', 'artist_6', 'artist_7', 'artist_8']] = a['artist(s)_name'].str.split(', ', expand=True)
print(a.head(5))


