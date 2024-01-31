import pandas as pd

df = pd.read_csv("spotify-2023.csv", encoding='latin1')
print(df.head(8))
print("Script executed successfully")
