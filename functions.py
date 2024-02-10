import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"

def taylors_version(df_cleaned):
    tays= df_cleaned[df_cleaned["artist(s)_name"]=="Taylor Swift"]
    print(tays)
    fig_dates= px.parallel_coordinates(tays, dimensions=["released_year", "released_month", "released_day"],color='in_spotify_charts',  title = "historial de taylor swift's most impresive records released date")
    fig_dates.show()
    fig_info = px.parallel_coordinates(tays, dimensions=["danceability_%", "valence_%", "energy_%", "acousticness_%", "instrumentalness_%", "liveness_%","speechiness_%"], title= "caracteristicas de las canciones mas top de tay", color="in_spotify_charts")
    fig_info.show()

def to_the_hits(df):
    print("seleccionaste lo que se necesita para ser un hit")

def streams_playlist(df):
    print()

def top_playlist(df_cleaned):
    top = df_cleaned
    top.rename(columns={"in_apple_playlists" : 'veces en playlist de apple', "track_name" : "cancion"}, inplace=True)
    top.rename(columns={"in_spotify_playlists" : 'veces en playlist de spotify', "track_name" : "cancion"}, inplace=True)
    print(top.head())
    order_by_spotify_playlist = top.sort_values(by="veces en playlist de spotify", ascending=False).head(15)
    order_by_apple_playlist = top.sort_values(by="veces en playlist de apple", ascending=False).head(15)
    apple = px.bar(order_by_apple_playlist, x='cancion', y = 'veces en playlist de apple', title='Top 15 canciones en playlist - ', color='artist(s)_name')
    spotify = px.bar(order_by_spotify_playlist, x='cancion', y='veces en playlist de spotify', title='Top 15 canciones en playlist - Spotify', color='cancion')
    apple.show()
    spotify.show()
def dates (df):
    print()
def duos(df):
    print()
def top_per_year(df):
    print()
