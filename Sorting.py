import pandas as pd

data = pd.read_csv("nba.csv")
print(data)
df = data.sort_values(["Team", "College"])
print(df.head(10))
df = data.sort_values(["Team", "College"], ascending=[True, True])
print(df.head(10))

