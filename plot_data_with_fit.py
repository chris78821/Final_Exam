"""
This plots a set of data with a fit curve and the points itself.
"""
__author__ = "Chris Thomack"

import numpy as np
import matplotlib.pyplot as plt
import fit_curve_array as fit_curve_array


def plot_data_with_fit(data_array, fit_curve, data_format="x", fit_format="--"):
    scatter_plot = plt.plot(data_array[0], data_array[1], data_format)
    curve_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format)
    return scatter_plot, curve_plot


if __name__ == "__main__":
    data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
    test_curve = [np.linspace(-2, 2), np.linspace(-2, 2) ** 2]
    plot_data_with_fit(data, test_curve)
    plt.show()