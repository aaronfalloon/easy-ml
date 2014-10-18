import kmeans
import pandas as pd
import cluster_evaluation
from scipy.cluster.vq import kmeans as scipy_kmeans, vq, whiten
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import pairwise_distances
import time

# Our data objects are rows in a DataFrame
data_objects = pd.read_csv("data/seeds.txt", delim_whitespace=True)

k = 3

time_1 = time.time()

print "My kmeans"

clusters = kmeans.kmeans(k, data_objects.ix[:, 0:7])

for i, cluster in enumerate(clusters):
    print "Cluster", i, len(cluster.data_objects)

print "Silhouette score", cluster_evaluation.silhouette_score(clusters)

time_2 = time.time()

print time_2 - time_1, "seconds"

print

time_1 = time.time()

print "Scipy kmeans"

data_objects = data_objects.ix[:, 0:7].as_matrix()

codebook, distortion = scipy_kmeans(data_objects, k)

code, distortion = vq(data_objects, codebook)

for i in range(k):
    print "Cluster", i, len(filter(lambda x:x==i, code))

print "Silhouette score", silhouette_score(data_objects, code)

time_2 = time.time()

print time_2 - time_1, "seconds"
