import pandas as pd

teams = pd.read_csv("./data/olympics/teams.csv")
medallists = pd.read_csv("./data/olympics/medallists.csv")

# Iterate through the rows of the 'medallists' DataFrame
#for index, row in medallists.iterrows():
    # Access and process row data here
    #print(row['name'], ': ', row['medal_type']) 

# Study mode
medal_counts = medallists.groupby('name')['medal_type'].count()
filtered_counts = medal_counts[medal_counts > 1]
sorted_counts = filtered_counts.sort_values(ascending=False)
top_5 = sorted_counts.head(5)

print('\n')
print('****** Top 5 Medalists *******')

print(top_5)

print('\n')
print('****** Medalists and their Teams *******')

#only_one = medallists[medallists['name'] == "McKEOWN Kaylee"].iloc[0]

duplicate_teams = []

for i, (athlete_name, count) in enumerate(top_5.items()):
    team_list = []
    for index, row in teams.iterrows():
        try:
            if isinstance(row['athletes'], str):
                if athlete_name in row['athletes']: 
                    duplicate_teams.append(row['team']) 
                    if row['team'] not in team_list: 
                        team_list.append(row['team'])
                        print(f"{athlete_name} -> {count}: {row['team']}")
        except AttributeError:
            print(row['team'])

print('\n')
print('******** Only Teams *********') 

for team in list(set(duplicate_teams)):
    print(team)

print('\n\n')

# Fluent mode 
#top_5 = medallists.groupby('name')['medal_type'].count()[medal_counts > 1].sort_values(ascending=False).head(5)
#print(top_5) 


# Transform DataFrame to list of lists
# medallists_list = medallists.values.tolist()

# Print the resulting list
# Print each value in the nested list
#for row in medallists_list:
    #print('****** NEXT ******')
    #for value in row: 
        #print(value)
