import pandas as pd

csv_file = './data/olympics/medallists.csv'
medalists_df = pd.read_csv(csv_file)

grouped_df = medalists_df.pivot_table(index='name', columns='medal_type', aggfunc='size', fill_value=0)

print(grouped_df)
