"""
Finds quadratic coefficients
"""

__author__ =  'Chris Thomack'

import numpy as np
from read_two_column_text import read_two_column_text


def calculate_quadratic_fit(data_array):
    x_values = data_array[0, :]
    y_values = data_array[1, :]
    quadratic_coefficients = np.polynomial.polynomial.polyfit(x_values, y_values, 2)
    return quadratic_coefficients


if __name__ == "__main__":
    data = np.array([np.linspace(-1, 1), np.linspace(-1, 1)**2])
    print(calculate_quadratic_fit(data))
    # print(calculate_quadratic_fit(read_two_column_text('volume_energies')))