import pandas as pd

data = pd.read_csv("nba.csv")
print(data)
(print(data.to_string()))
print(data.head((10)))

# groupby
gp = data.groupby("Team").sum('Salary')
print(gp.head(10))
gp = data.groupby("Team").min('Salary')
print(gp.head(10))
gp = data.groupby("Team").max('Salary')
print(gp.head(10))
gp = data.groupby("Team").mean('Salary')
print(gp.head(10))   
