import random
import math
import copy

"""
kmeans for integer data objects in 1-dimensional space
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
            self.centroid = sum(self.data_objects) / len(self.data_objects)
        except:
            # When no data objects have been assigned, don't update the
            # centroid
            pass


    def distance_to(self, data_object):
        return math.fabs(self.centroid - data_object)


def assign_data_objects_to_clusters(clusters, data_objects):
    if len(clusters) < 1:
        raise Error("No cluster objects")

    if len(data_objects) < 1:
        raise Error("No data objects")

    # Assign each data object to a cluster
    for data_object in data_objects:
        closest_cluster = clusters[0]

        for i, cluster in enumerate(clusters):
            if cluster.distance_to(data_object) < closest_cluster.distance_to(data_object):
                closest_cluster = cluster

        closest_cluster.assign_data_object(data_object)


def update_centroids(clusters):
    for cluster in clusters:
        cluster.update_centroid()


def kmeans(k, data_objects):
    clusters = []

    # Give each cluster a random centroid
    for _ in range(k):
        centroid = random.randint(min(data_objects), max(data_objects))
        clusters.append(Cluster(centroid))

    # Perform initial assignments
    assign_data_objects_to_clusters(clusters, data_objects)

    previous_clusters = copy.deepcopy(clusters)

    update_centroids(clusters)

    # And minimise...
    while clusters != previous_clusters:
        # Now that the centroids have changed, all data objects should be
        # unassigned
        for cluster in clusters:
            cluster.unassign_data_objects()

        assign_data_objects_to_clusters(clusters, data_objects)

        # Update previous clusters
        previous_clusters = copy.deepcopy(clusters)

        update_centroids(clusters)

        for i, cluster in enumerate(clusters):
            print "interim", i, cluster.data_objects

    for i, cluster in enumerate(clusters):
        print "final", i, cluster.data_objects


data_objects = [8, 1, 3, 2, 7, 6, 8, 9, 90, 90, 45, 43, 42, 200, 250,
        20, 8, 9, 800, 80, 550, 678]

kmeans(4, data_objects)
