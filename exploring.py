import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"

df = pd.read_csv("spotify-2023.csv", encoding='latin1')

pd.set_option('display.max_rows', None)    
pd.set_option('display.max_columns', None)
#print(df.info())
#print(df.dtypes)
#print(df.head())
df.dropna()
df['release_date'] = df['released_year'].astype(str) + '-' + df['released_month'].astype(str) + '-' + df['released_day'].astype(str)
df.sort_values(by = 'release_date', inplace=True )
#print(df.head())
date = df['release_date']
a = pd.DataFrame(df['release_date'], columns = 'release_date')

a["times"] = df.value_counts(df['release_date'],ascending=False).head()
fig = px.bar(df,
            x = 'release_date',
            y = (df.value_counts(df['release_date'])),
            title= 'Fechas con mas canciones sacadas',
            color = 'streams',
            color_continuous_scale='Picnic' )
fig.show()




