"""
Mean-Variance-Standard Deviation Calculator
Takes a list and convert it to 3x3 numpy array and then give out mean, variance, standard deviation,
min and max.
"""

import numpy as np


def calculate(list):  # pylint: disable=redefined-builtin
    """Converts to 3x3 numpy array and then calculate"""
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Create a numpy array with 3x3 dimension
    np_list = np.array(list).reshape((3, 3))

    # for the mean
    np_list_mean = [
        np.mean(np_list, axis=0).tolist(),
        np.mean(np_list, axis=1).tolist(),
        np.mean(np_list),
    ]

    # for the variance
    np_list_variance = [
        np.var(np_list, axis=0).tolist(),
        np.var(np_list, axis=1).tolist(),
        np.var(np_list),
    ]

    # for standard deviation
    np_list_standard_deviation = [
        np.std(np_list, axis=0).tolist(),
        np.std(np_list, axis=1).tolist(),
        np.std(np_list),
    ]

    # for the max
    np_list_max = [
        np_list.max(axis=0).tolist(),
        np_list.max(axis=1).tolist(),
        np_list.max(),
    ]

    # for the min
    np_list_min = [
        np_list.min(axis=0).tolist(),
        np_list.min(axis=1).tolist(),
        np_list.min(),
    ]

    # for the sum
    np_list_sum = [
        np.sum(np_list, axis=0).tolist(),
        np.sum(np_list, axis=1).tolist(),
        np.sum(np_list),
    ]

    calculations = {
        "mean": np_list_mean,
        "variance": np_list_variance,
        "standard deviation": np_list_standard_deviation,
        "max": np_list_max,
        "min": np_list_min,
        "sum": np_list_sum,
    }

    return calculations
