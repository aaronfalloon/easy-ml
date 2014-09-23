import csv
import matplotlib.pyplot as plt
import random
import math
import pandas
from pandas import DataFrame

aus_open = pandas.read_csv('data/AusOpen-men-2013.csv')

aus_open = aus_open.dropna()

print aus_open

joined_data = DataFrame()

plt.plot(aus_open['ACE.1'], aus_open['ACE.2'], 'o')
plt.xlabel('Aces player 1')
plt.ylabel('Aces player 2')

plt.show()

k = 3

cluster_centers = []

# Create the cluster centers
for i in range(k):
    cluster_center = ClusterCenter((random.randint(min(aces), max(aces)), random.randint(min(double_faults), max(double_faults))))
    cluster_centers.append(cluster_center)

# Plot the cluster start positions
for cluster_center in cluster_centers:
    plt.plot(cluster_center.x, cluster_center.y, 'bx')

# Assign each data point to a cluster
cluster_assignments = []

for i in range(len(aces)):
    distances = []

    # Get the data point's distance from each cluster center
    for cluster_center in cluster_centers:
        distance = math.sqrt((cluster_center.x - aces[i]) ** 2 + (cluster_center.y - double_faults[i]) ** 2)

        distances.append(distance)

    cluster_assignments.append(distances.index(min(distances)))

# Work out the new positions of each cluster
updated_k_positions = []

class ClusterCenter:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_cluster_center(self, cluster_center):
        self.cluster_center = cluster_center

for i in range(k):
    x_distances = []
    y_distances = []
    count = 0

    for j in range(len(cluster_assignments)):
        if cluster_assignments[j] == i:
            x_distances.append(aces[j])
            y_distances.append(double_faults[j])
            count += 1

    if count > 0:
        updated_k_positions.append(((sum(x_distances) / count), (sum(y_distances) / count)))

# Plot the cluster updated positions
for updated_position in updated_k_positions:
    plt.plot(updated_position[0], updated_position[1], 'gx')

plt.show()
