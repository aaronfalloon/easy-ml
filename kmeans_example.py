import kmeans
import pandas as pd
import cluster_evaluation

# Our data objects are rows in a DataFrame
data_objects = pd.read_csv("data/seeds.txt", delim_whitespace=True)

clusters = kmeans.kmeans(3, data_objects.ix[:, 0:7])

for i, cluster in enumerate(clusters):
    print "Cluster", i, len(cluster.data_objects)

cluster_evaluation.silhouette(clusters)
