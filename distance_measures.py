import numpy as np

def euclidean(data_object_1, data_object_2):
    return np.sqrt(np.sum(np.square(np.subtract(data_object_1, data_object_2))))
