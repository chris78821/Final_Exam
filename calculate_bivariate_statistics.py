"""
Return statistics on a set of data.
"""

__author__ =  'Chris Thomack'

import numpy as np
from scipy import stats


def calculate_bivariate_statistics(data_array):  # data_array is from read_two_column_text
    if len(data_array) != 2 or len(data_array[0]) <= 1:
        raise IndexError
    statties = stats.stats.describe(data_array, axis=1)
    mean_y = statties.mean[1]
    x_min, y_min = statties.minmax[0][0], statties.minmax[0][1]
    x_max, y_max = statties.minmax[-1][0], statties.minmax[-1][1]
    standard_deviation_of_y = np.sqrt(statties.variance[1])
    statistics = np.array([mean_y, standard_deviation_of_y, x_min, x_max, y_min, y_max])
    return statistics


if __name__ == "__main__":
    x_array = np.linspace(-10, 10, 1000000)
    y_array = x_array ** 2
    stats = calculate_bivariate_statistics([x_array, y_array])
    print(f'test_statistics={stats}')
    print(np.mean(y_array))
    print(np.mean(x_array))
    print(np.std(y_array))