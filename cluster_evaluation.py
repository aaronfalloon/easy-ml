from pandas import DataFrame
import distance_measures
import numpy as np
import copy

def silhouette_score(clusters):
    if len(clusters) < 1:
        raise Error("No Cluster objects")

    silhouette_scores = []

    for i, cluster in enumerate(clusters):
        data_objects = DataFrame(cluster.data_objects)

        for j, selected_data_object in data_objects.iterrows():
            data_objects_minus_selected = data_objects.drop(j)

            # Get the data object's average dissimilarity to all the other data
            # objects in its cluster
            own_cluster_dissimilarity = get_average_dissimilarity(data_objects_minus_selected, selected_data_object)

            dissimilarity_neighbouring_clusters = []

            # Get the data object's average dissimilarity to the data objects
            # in the other clusters
            for j, neighbouring_cluster in enumerate(clusters):
                # Don't work it out for the cluster the data object is assigned
                # to
                if i == j:
                    continue

                dissimilarity_neighbouring_clusters.append(get_average_dissimilarity(DataFrame(neighbouring_cluster.data_objects), selected_data_object))

            # Figure out the data object's neighbouring cluster
            neighbouring_cluster_dissimilarity = min(dissimilarity_neighbouring_clusters)

            divisor = max(own_cluster_dissimilarity, neighbouring_cluster_dissimilarity)

            # Now work out the silhouette
            silhouette_score = (neighbouring_cluster_dissimilarity - own_cluster_dissimilarity) / divisor

            silhouette_scores.append(silhouette_score)

    return np.mean(silhouette_scores)


def get_average_dissimilarity(data_objects, selected_data_object):
    distances = []

    for _, data_object in data_objects.iterrows():
        distances.append(distance_measures.euclidean(selected_data_object, data_object))

    return np.mean(distances)
