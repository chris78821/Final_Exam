"""
This prints x and y values in an array which the y values are computed by the quadratic equation
"""

__author__ =  'Chris Thomack'

import numpy as np
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_bivariate_statistics import calculate_bivariate_statistics
from read_two_column_text import read_two_column_text


def fit_curve_array(quadratic_coefficients, x_min, x_max, number_of_points=50):
    if x_max < x_min:
        # if x_max < x_min:
        raise ArithmeticError
    if number_of_points <= 2:
        raise IndexError
    x_values = np.linspace(x_min, x_max, number_of_points)
    y_values = np.polynomial.polynomial.polyval(x_values, quadratic_coefficients)
    fit_curve = np.array([x_values, y_values])
    return fit_curve


if __name__ == "__main__":
    test_coefficients = [0, 0, 1]
    print(fit_curve_array(test_coefficients, -2, 2, 5))