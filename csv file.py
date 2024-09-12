
import pandas as pd
import numpy as np

data = pd.read_csv("nba.csv")
print(data)
print("========================head============================================================================")
print(data.head(10))        # 10 form top

print("========================tail===============================================================================")
print(data.tail(10))        # 10 from bottom

print("=======================info=================================================================================")
print(data.info())

print("======================describe===============================================================================")
print(data.describe())

print("===================Name duplicates=============================================================================")
print(data["Name"].duplicated())        # duplicates

print("===================Name sum of the duplicates================================================================")
print(data["Name"].duplicated().sum())      # sum of the duplicates

print("===================Team duplicates========================================================================")
print(data["Team"].duplicated())

print("=============Team sum of the duplicates================================================================")
print(data["Team"].duplicated().sum())

print("======================drop_duplicates========================================================================")
print(data.drop_duplicates("Team"))

print("=========================replace===========================================================================")
print(data.replace(np.nan, "Hello"))

print("=========================replace a particular value==========================================================")
data["Team"] = data["Team"].replace(np.nan, "Good Morning")
print(data)

print("=========================mean of age==========================================================")
print(data["Age"].mean())

print("=========================fillna==========================================================")
print(data.fillna(method = "bfill"))

# Example 1: Extracting single Row
data = pd.read_csv("nba.csv", index_col="Name")     # making dataframe from csv file

first = data.loc["Avery Bradley"]       # retrieving row by loc method
second = data.loc["R.J. Hunter"]
print(first, "\n\n\n", second)
print("===========================================================================================================")

# Example 2: Multiple parameters
data = pd.read_csv("nba.csv", index_col="Name")
rows = data.loc[["Avery Bradley","R.J. Hunter"]]
print(type(rows))   # checking data type of rows
rows
print("===========================================================================================================")

# Example 3: Extracting multiple rows with same index
data = pd.read_csv("nba.csv", index_col="Team")
rows = data.loc["Utah Jazz"]       # retrieving rows by loc method

print(type(rows))   # checking data type of rows
rows

h=data.isnull()
print(h)
