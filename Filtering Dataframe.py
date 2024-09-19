import pandas as pd

data = pd.read_csv("nba.csv")
print(data)

df = data['Team'] == 'Boston Celtics'   
print(df)    #this is a boolean series because the output will be either true or false
print(type(df))

mask = data['Team'] == 'Boston Celtics'
print(data[mask])
print(data[mask].shape[0])

def team_count(team):
    mask = data['Team'] == team
    return data[mask].shape[0]  

print(team_count('Boston Celtics'))
