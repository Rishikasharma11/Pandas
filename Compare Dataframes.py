import pandas as pd

data = {
        "Fruits" : ["Mango", "Apple", "Banana", "Kiwi", "Graphes"],
        "Price" : [80, 160, 60, 110, 80],
        "Quantity" : [7, 20, 12, 5, 35]
        }

df1 = pd.DataFrame(data)
print(df1)

df2 = df1.copy()
df2.loc[0, "Price"] = 120
df2.loc[3, "Price"] = 80
df2.loc[0, "Quantity"] = 9
df2.loc[3, "Quantity"] = 7
print(df2)


# Compare
print(df1.compare(df2))
print(df1.compare(df2, keep_equal=True))
