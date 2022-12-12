import numpy as np


def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  else:

    # Create a numpy array with 3x3 dimension
    np_list = np.array(list).reshape((3, 3))

    # for the mean
    mean_axis_1 = np.mean(np_list, axis=0).tolist()
    mean_axis_2 = np.mean(np_list, axis=1).tolist()
    mean_flattened = np.mean(np_list)
    mean = [mean_axis_1, mean_axis_2, mean_flattened]

    # for the variance
    variance_axis_1 = np.var(np_list, axis=0).tolist()
    variance_axis_2 = np.var(np_list, axis=1).tolist()
    variance_flattened = np.var(np_list)
    variance = [variance_axis_1, variance_axis_2, variance_flattened]

    # for standard deviation
    standard_deviation_axis_1 = np.std(np_list, axis=0).tolist()
    standard_deviation_axis_2 = np.std(np_list, axis=1).tolist()
    standard_deviation_flattened = np.std(np_list)
    standard_deviation = [
      standard_deviation_axis_1, standard_deviation_axis_2,
      standard_deviation_flattened
    ]

    # for the max
    max_axis_1 = np_list.max(axis=0).tolist()
    max_axis_2 = np_list.max(axis=1).tolist()
    max_flattened = np_list.max()
    max = [max_axis_1, max_axis_2, max_flattened]

    # for the min
    min_axis_1 = np_list.min(axis=0).tolist()
    min_axis_2 = np_list.min(axis=1).tolist()
    min_flattened = np_list.min()
    min = [min_axis_1, min_axis_2, min_flattened]

    # for the sum
    sum_axis_1 = np.sum(np_list, axis=0).tolist()
    sum_axis_2 = np.sum(np_list, axis=1).tolist()
    sum_flattened = np.sum(np_list)
    sum = [sum_axis_1, sum_axis_2, sum_flattened]

    calculations = {
      'mean': mean,
      'variance': variance,
      'standard deviation': standard_deviation,
      'max': max,
      'min': min,
      'sum': sum
    }

    return calculations
