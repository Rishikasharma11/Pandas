import pandas as pd

data1 = {
    "Empl id" : ["Ep01", "Ep02", "Ep03", "Ep04", "Ep05", "Ep06"],
    "Names" : ["Rishika", "Sanaya", "Manas", "Harsh", "Janhavi", "Mayank"],
    "Age" : [34, 22, 26, 29, 31, 27]
}

data2 = {
    "Empl id" : ["Ep07", "Ep08", "Ep09", "Ep10", "Ep11", "Ep12"],
    "Names" : ["Riya", "Shrishti", "Anand", "Pratik", "Vivek", "Ayushi"],
    "Age" : [25, 27, 32, 26, 29, 34]
}

df1 = pd.DataFrame(data1)
print(df1)
df2 = pd.DataFrame(data2)
print(df2)

print(pd.concat([df1, df2]))
