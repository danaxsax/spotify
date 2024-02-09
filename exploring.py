import pandas as pd

df = pd.read_csv("spotify-2023.csv", encoding='latin1')

pd.set_option('display.max_rows', None)    
pd.set_option('display.max_columns', None)
print(df.info())
print(df.dtypes)
print(df.head())
df_cleaned = df.dropna()
order_by_spotify_playlist = df.sort_values(by="in_spotify_playlists", ascending=False).head(5)
order_by_apple_playlist = df.sort_values(by="in_apple_playlists", ascending=False).head(5)
tracks_name = ''
for row in order_by_apple_playlist:
    tracks_name += order_by_apple_playlist["track_name"]
print(tracks_name)

