import pandas as pd

data = pd.read_csv("nba.csv")
print(data)
# Drop duplicate will delete the duplicate parameters of a particular column
dd = data.drop_duplicates(subset=['Team'])
print(dd)
print(dd.shape)
dd = data.drop_duplicates(subset=['Team', 'Height'])
print(dd)
print(dd.shape)
