import pandas as pd

x = ['Virat', 'Rohit', 'Hardik', 'Jadeja']
df = pd.DataFrame(x)
print(df)

data = {
    "Name" : ["Rishika", "Shruti", "Kirti"],
    "Age" : [22, 20, 18],
    "Location" : ["Indore", "Khandwa", "Bhopal"]
}

df = pd.DataFrame(data)
print(df)


