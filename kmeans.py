import random
import math
import copy
import pandas as pd
from pandas import DataFrame
import numpy as np

"""
kmeans for n-dimensional data objects of integers and floats.
"""

class Cluster:
    def __init__(self, centroid):
        self.centroid = centroid
        self.data_objects = []


    def __eq__(self, other_cluster):
        return self.centroid == other_cluster.centroid


    def assign_data_object(self, data_object):
        self.data_objects.append(data_object)


    def unassign_data_objects(self):
        self.data_objects = []


    def update_centroid(self):
        try:
            # Convert to DataFrame for easier calculations
            data_objects = pd.DataFrame(self.data_objects)

            self.centroid = data_objects.mean(0)
        except:
            # When no data objects have been assigned, don't update the
            # centroid
            pass


    def distance_to(self, data_object):
        return np.sqrt(np.sum(np.square(np.subtract(self.centroid, data_object))))


def assign_data_objects_to_clusters(clusters, data_objects):
    if len(clusters) < 1:
        raise Error("No Cluster objects")

    if len(data_objects) < 1:
        raise Error("No data objects")

    # Assign each data object to a cluster
    for index, data_object in data_objects.iterrows():
        closest_cluster = clusters[0]

        for i, cluster in enumerate(clusters):
            # Work out the distance of the data object from the cluster centroid
            if cluster.distance_to(data_object) < closest_cluster.distance_to(data_object):
                closest_cluster = cluster

        closest_cluster.assign_data_object(data_object)


def update_centroids(clusters):
    for cluster in clusters:
        cluster.update_centroid()


def are_cluster_lists_identical(cluster_list_1, cluster_list_2):
    identical = True

    # If the lists aren't the same length, they can't be identical
    if len(cluster_list_1) != len(cluster_list_2):
        return False

    # Compare the centroids of the clusters in each list
    for i in range(len(cluster_list_1)):
        values_equal = cluster_list_1[i].centroid.eq(cluster_list_2[i].centroid)

        if not values_equal.all():
            identical = False
            break

    return identical


def kmeans(k, data_objects):
    clusters = []

    min_values = data_objects.min(axis=0)
    max_values = data_objects.max(axis=0)

    # Give each cluster a random centroid
    for _ in range(k):
        values = []

        # Get a random value for each cell
        for i in range(len(data_objects.columns)):
            value = random.uniform(min_values[i], max_values[i])
            values.append(value)

        clusters.append(Cluster(pd.Series(values)))

    # Perform initial assignments
    assign_data_objects_to_clusters(clusters, data_objects)

    previous_clusters = copy.deepcopy(clusters)

    update_centroids(clusters)

    # And minimise...
    while not are_cluster_lists_identical(clusters, previous_clusters):
        # Now that the centroids have changed, all data objects should be
        # unassigned
        for cluster in clusters:
            cluster.unassign_data_objects()

        assign_data_objects_to_clusters(clusters, data_objects)

        # Update previous clusters
        previous_clusters = copy.deepcopy(clusters)

        update_centroids(clusters)

    return clusters
