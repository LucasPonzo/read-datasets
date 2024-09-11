import pandas as pd

teams = pd.read_csv("./data/olympics/teams.csv")
medallists = pd.read_csv("./data/olympics/medallists.csv")

# Study mode
medal_counts = medallists.groupby('name')['medal_type'].count()
tops = medal_counts[medal_counts > 1].sort_values(ascending=False).head(10)

print('\n')
print('****** Top 10 Medalists *******')

print(tops)

print('\n')
print('****** Medalists and their Teams *******')

duplicate_teams = []

for i, (athlete_name, count) in enumerate(tops.items()):
    team_list = []
    # Performance test 
    for index, row in teams.iterrows():
        try:
            if isinstance(row['athletes'], str):
                if athlete_name in row['athletes']: 
                    duplicate_teams.append(row['team']) 
                    if row['team'] not in team_list: 
                        team_list.append(row['team'])
                        print(f"{athlete_name} -> Qty of Medals: {count} -> Team: {row['team']}")
        except AttributeError:
            print(row['team'])

print('\n')
print('******** Only Teams *********') 

# Create a distinct list 
for team in list(set(duplicate_teams)):
    print(team)

print('\n\n')
