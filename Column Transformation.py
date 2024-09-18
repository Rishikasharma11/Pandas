import pandas as pd

data = pd.read_csv("nba.csv")
print(data)
(print(data.to_string()))

# Merging name and college column
data["Name and College"] = data["Name"].str.capitalize() + " " + data["College"]
print(data)

data.loc[(data["Age"] > 25), "Adults"] = "Yes"
data.loc[(data["Age"] <= 25), "Adults"] = "No"
print(data.head(5))

months = {"Months":["January", "Febuary", "March", "April", "May", "June"]}
a = pd.DataFrame(months)
print(a)

# Below statement will through an error
'''
a["Short"] = a["Months"].str.a[0:3]
print(a)
'''

# here we will use mapping
def extract(value):
    return value[0:3]

a["Short_Months"] = a["Months"].map(extract)
print(a)

