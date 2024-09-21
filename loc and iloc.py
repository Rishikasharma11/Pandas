# loc -
# iloc - indexing loc
import pandas as pd

data = pd.read_csv("nba.csv")
print(data)
(print(data.to_string()))

data.loc[(data["Age"] > 25), "Adults"] = "Yes"
data.loc[(data["Age"] <= 25), "Adults"] = "No"
print(data.head(5))

print(data.iloc[1])
print(data.iloc[1:3])
print(data.iloc[1:11:2])
print(type(data.iloc[1:3]))
