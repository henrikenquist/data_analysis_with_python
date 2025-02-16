import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    # Reshape list into a 3x3 matrix using numpy, and then flatten it.
    a = np.reshape(np.array(list), [3,3])
    flattened = np.ndarray.flatten(a) # creates a copy
    print(f"{a=}")
    print(f"{flattened=}")
    # Alternatives:
    # flattened = np.reshape(-1) # creates a copy if necessary
    # flattened = np.ravel(a) # creates a copy

    # Calculate mean, variance, standard deviation, max, min and sum along the rows, columns and flattened array.
    calculations = {
        'mean': [np.mean(a,axis=0).tolist(), np.mean(a,axis=1).tolist(), np.mean(flattened).tolist()],
        'variance': [np.var(a,axis=0).tolist(), np.var(a,axis=1).tolist(), np.var(flattened).tolist()],
        'standard deviation': [np.std(a,axis=0).tolist(), np.std(a,axis=1).tolist(), np.std(flattened).tolist()],
        'max': [np.max(a,axis=0).tolist(), np.max(a,axis=1).tolist(), np.max(flattened).tolist()],
        'min': [np.min(a,axis=0).tolist(), np.min(a,axis=1).tolist(), np.min(flattened).tolist()],
        'sum': [np.sum(a,axis=0).tolist(), np.sum(a,axis=1).tolist(), np.sum(flattened).tolist()]
        }

    return calculations