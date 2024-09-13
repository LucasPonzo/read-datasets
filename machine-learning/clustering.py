import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("./data/olympics/medallists.csv")

# Group by gender, medal type, country, and discipline, then count occurrences
medal_counts = df.groupby(["gender", "medal_type", "country", "discipline"]).size().reset_index(name="Count")
filtered_medal_counts = medal_counts[medal_counts["Count"] > 1].sort_values(by="Count", ascending=False)

# Print the results
print(filtered_medal_counts)

#
athletes = []

for index, row in filtered_medal_counts.iterrows():
    # Filter the original DataFrame based on the current row's values
    filtered_df = df[
        (df["gender"] == row["gender"]) &
        (df["medal_type"] == row["medal_type"]) &
        (df["country"] == row["country"]) &
        (df["discipline"] == row["discipline"])
    ]
    # Append the relevant columns from filtered_df to athletes
    athletes.append(filtered_df[["country", "medal_type", "discipline", "name", "gender"]])

print('\n')
print('***** The Athletes ******')
print('\n')

# Sort athletes by country and then by name
sorted_athletes = sorted(athletes, key=lambda x: (x['medal_type'].iloc[0], x['country'].iloc[0]))

for athlete_group in sorted_athletes:
    print('\n')
    print(athlete_group) 

