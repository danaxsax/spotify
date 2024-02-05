import pandas as pd

df = pd.read_csv("spotify-2023.csv", encoding='latin1')
#print(df.info())
#print(df.dtypes)
#print(df['artist(s)_name'].value_counts)
#print(df.notna().all())
#print(df[df['in_shazam_charts'].isnull()])
#print(df["artist(s)_name"]ss)
#print(f"original dataframe")
#print(df.head(8))
#print(f"****************************************************************")

print(f"columns with null values")

pd.set_option('display.max_rows', None)   
pd.set_option('display.max_columns', None)
print((df.notna().all()))
#print(f"****************************************************************")
#print(df["bpm"].max())

#bpm_160 = df[df["bpm"]>160]
#print (bpm_160)
