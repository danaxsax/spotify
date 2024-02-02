import pandas as pd

df = pd.read_csv("spotify-2023.csv", encoding='latin1')
#print(df.head(8))
#print(df['artist(s)_name'].value_counts)
#print(df.notna().all())
#print(df[df['in_shazam_charts'].isnull()])
#print(df["artist(s)_name"]ss)
print(f"original dataframe")
print(df.head(8))
print(f"****************************************************************")

print(f"columns with null values")
print((df.notna().all()))
print(f"****************************************************************")

print(f"dataframe with marked null values for empty registers")
df_filled = df.fillna(value=0)
print (df_filled)
print(f"****************************************************************")

print(f"dataframe full")
nan_rows_after = df_filled[df_filled.isna().any(axis=1)]
print(nan_rows_after)
print(f"****************************************************************")



