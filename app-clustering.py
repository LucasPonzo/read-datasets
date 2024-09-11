import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline

# 1. Load and Prepare Data
medallists = pd.read_csv("./data/olympics/medallists.csv")

# Feature Selection
features = medallists[['medal_type', 'gender', 'country', 'nationality', 'team_gender', 'discipline']].copy()

# 2. Feature Encoding
# Create a ColumnTransformer for one-hot encoding categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), 
         ['medal_type', 'gender', 'country', 'nationality', 'team_gender', 'discipline'])
    ]
)

# 3. Determine Optimal Number of Clusters (Optional)
# You can use techniques like the elbow method or silhouette analysis to find a suitable k value.
# For this example, let's assume you've determined k=5 to be appropriate.
k = 5

# 4. K-Means Clustering
# Create the KMeans model
kmeans = KMeans(n_clusters=k, random_state=42)  # Set random_state for reproducibility

# Create a pipeline
pipeline = make_pipeline(preprocessor, kmeans)

# Fit the model 
pipeline.fit(features)

# 5. Get Cluster Labels
# Add cluster labels to your DataFrame
medallists['cluster'] = pipeline.predict(features)

# 6. Analyze Clusters
cluster_modes = medallists.groupby('cluster').agg(pd.Series.mode)

for cluster_id, cluster_data in cluster_modes.iterrows():
    print(f"Cluster {cluster_id}:")
    for col in cluster_data.index:
        print(f"  - {col}: {cluster_data[col]}")
    print("-" * 20)

# ... (Further analysis and visualization based on your insights) ...
