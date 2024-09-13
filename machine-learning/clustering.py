import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("./data/olympics/medallists.csv")

# Group by gender, medal type, country, and discipline, then count occurrences
medal_counts = df.groupby(["gender", "medal_type", "country", "discipline"]).size().reset_index(name="Count")
filtered_medal_counts = medal_counts[medal_counts["Count"] > 1].sort_values(by="Count", ascending=False)

# 1. Feature Engineering
country_medal_counts = medal_counts.groupby("country")["Count"].agg(["sum", "mean", "std"]).reset_index()
country_medal_counts.columns = ["country", "total_medals", "mean_medals", "std_medals"]

# 2. Data Preprocessing
features = ["total_medals", "mean_medals", "std_medals"]

# 2.1. Drop NaN values 
country_medal_counts.dropna(subset=features, inplace=True)

scaler = StandardScaler()
country_medal_counts[features] = scaler.fit_transform(country_medal_counts[features])

# 3. DBSCAN Clustering 
dbscan = DBSCAN(eps=0.5, min_samples=5)  # Adjust eps and min_samples
country_medal_counts["cluster"] = dbscan.fit_predict(country_medal_counts[features])

country_medal_counts_sorted = country_medal_counts.sort_values(by="cluster")

#  Print the Countries of Cluster 0
print(country_medal_counts_sorted[country_medal_counts_sorted["cluster"] == 0])

# Print Countries of all Clusters 
# print(country_medal_counts_sorted[country_medal_counts_sorted["cluster"] == 0])

#     gender    medal_type        country     discipline  Count
#267  Female  Silver Medal         Brazil       Football     22
#660    Male    Gold Medal          Spain       Football     22
#726    Male  Silver Medal         France       Football     21
#33   Female  Bronze Medal          China       Swimming     21
#251  Female    Gold Medal  United States       Football     20

# athletes = []

#for index, row in filtered_medal_counts.iterrows():
    # Filter the original DataFrame based on the current row's values
    #filtered_df = df[
        #(df["gender"] == row["gender"]) &
        #(df["medal_type"] == row["medal_type"]) &
        #(df["country"] == row["country"]) &
        #(df["discipline"] == row["discipline"])
    #]
    # Append the relevant columns from filtered_df to athletes
    #athletes.append(filtered_df[["country", "medal_type", "discipline", "name", "gender"]])

print('\n')
#print('***** The Athletes ******')
print('\n')

# Sort athletes by country and then by name
#sorted_athletes = sorted(athletes, key=lambda x: (x['medal_type'].iloc[0], x['country'].iloc[0]))[:5]

# Print each sorted group 
#for athlete_group in sorted_athletes:
    #print('\n')
    #print(athlete_group) 

# Example group
#      country medal_type   discipline           name             gender
#902   Italy  Silver Medal  Artistic Gymnastics  ANDREOLI Angela  Female
#903   Italy  Silver Medal  Artistic Gymnastics    D'AMATO Alice  Female
#904   Italy  Silver Medal  Artistic Gymnastics  ESPOSITO Manila  Female
#905   Italy  Silver Medal  Artistic Gymnastics      IORIO Elisa  Female
#906   Italy  Silver Medal  Artistic Gymnastics    VILLA Giorgia  Female
