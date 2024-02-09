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
    playlist = df_cleaned[df_cleaned["in_spotify_playlists"].max()  ]
    print(playlist)
    print()
def dates (df):
    print()
def duos(df):
    print()
def top_per_year(df):
    print()
