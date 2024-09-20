import pandas as pd

unique = pd.Series([2, 1, 3, 3])
print(pd.unique(unique))

# unique() works only for one-dimensional data (Series or one column of a DataFrame).
