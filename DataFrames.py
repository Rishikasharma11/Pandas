import pandas as pd

data = {
    "Name" : ["Rishika", "Shruti", "Kirti"],
    "Age" : [22, 20, 18],
    "Location" : ["Indore", "Khandwa", "Bhopal"]
}

df = pd.DataFrame(data)
print(df)
