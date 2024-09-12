# Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
import pandas as pd
import numpy as np

ser = pd.Series()
print(ser)

info = np.array(['P', 'A', 'N', 'D', 'A', 'S'])
x = pd.Series(info)
print(x)

game = np.array(['C','R', 'I', 'C', 'K', 'E', 'T'])
x = pd.Series(game)
print(x)

subject = np.array(['S', 'C', 'I', 'E', 'N', 'C', 'E'])
x = pd.Series(subject, index=[10, 11, 12, 13, 14, 15, 16])         
print("Indexing:\n", x)                  # Indexing
print("Printing through index number:\n", x[12])              # Printing through index number
print("Accessing element of Series:\n", x[:4])              # Accessing element of Series

ser1 = pd.Series(np.linspace(3, 33, 3))
print(ser1)

ser2 = pd.Series(range(10))
print(ser2)

ser3 = pd.Series(range(1, 20, 3), index= [x for x in 'abcdefg'])
print(ser3)

ser4 = np.arange(10, 15)
ser4Obj = pd.Series(data = ser4*5, index=ser4)
print(ser4Obj)
