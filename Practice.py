import pandas as pd
import numpy as np

data = {'Values': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Calculate cumulative sum
df['Cumulative_Sum'] = df['Values'].cumsum()
print(df)
df['Cumulative_Product'] = df['Values'].cumprod()
print(df)

# --------------------------------------------------------Series------------------------------------------------------------
# converting series to list
d = pd.Series([1, 2, 3, 4])
print(d)
print(type(d))
print(type(d.tolist))

# converting series to array
ser = pd.Series([1,3, 5, 7])
print(type(ser))
arr = np.array(ser)
print(type(arr))

# Write a Pandas program to convert Series of lists to one Series.
ser1 = pd.Series(['Red', 'Green', 'White'])
ser2 = pd.Series(['Red', 'Black'])
ser3 = pd.Series(['Yellow'])
print(pd.concat((ser1, ser2, ser3)))

# Write a Pandas program to sort a given Series.
series_to_sort = pd.Series(['100', '200', 'python', '300.12', '400'])
sorted_series = series_to_sort.sort_values()
print(sorted_series)

# Write a Pandas program to add some data to an existing Series.
new_series = pd.Series(['500', 'PHP'])
adding_to_series_to_sort = pd.concat((series_to_sort, new_series))
print(adding_to_series_to_sort)
 
# ----------------------------------------------------------------DataFrame--------------------------------------------------------------
# 1. Write a Pandas program to create a dataframe from a dictionary and display it.

sample_data = {'X':[78,85,96,80,86], 
              'Y':[84,94,89,83,86],
              'Z':[86,97,96,72,83]}
print(type(sample_data))
sample_data_df = pd.DataFrame(sample_data)
print(sample_data_df)
print(type(sample_data_df))

# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
exam_data =  {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print(df)

# 3. Write a  Pandas program to display a summary of the basic information about a specified DataFrame and its data.
print(df.info())

# 4. Write a Pandas program to get the first 3 rows of a given DataFrame.
print(df.head(3))       # or
print(df.iloc[: 3])

# 5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
print(df[['name', 'score']])

# 6. Write a Pandas program to select the specified columns and rows from a given data frame.
print(df.iloc[[1, 3, 5, 6], [1,3]])

# 7. Write a  Pandas program to select the rows where the number of attempts in the examination is greater than 2.
print(df.loc[df['attempts'] > 2])

# 8. Write a Pandas program to count the number of rows and columns of a DataFrame.
print(df.shape)

# 9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
print(df.loc[df['score'].isnull()])

# 10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
print(df.loc[(df['score'] >= 15) & (df['score'] <= 20)])
print(df.loc[df['score'].between(15,20)])       # or

# 11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
print(df.loc[(df['attempts'] > 2) & (df['score'] < 15)])

# 12. Write a Pandas program to change the score in row 'd' to 11.5.
df.loc['d', 'score'] = 11.5
print(df)

# Write a  Pandas program to calculate the sum of the examination attempts by the students.
print("Sum of the examination attempts by the students:  \n", df['attempts'].sum())

# 14. Write a Pandas program to calculate the mean of all students' scores. Data is stored in a dataframe.
print("Mean score for each different student in data frame: \n", df['score'].mean())

# 15. Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]
print(df)