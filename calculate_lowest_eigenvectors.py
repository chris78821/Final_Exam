"""
Calculates lowest eigenvector and eigenvalue of a matrix.
"""

__author__ = 'Chris Thomack'

import numpy as np


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    eigenvalues = (np.linalg.eig(square_matrix)[0])[:number_of_eigenvectors]
    eigenvectors = (np.linalg.eig(square_matrix)[1])[:number_of_eigenvectors]
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    test_matrix = [[2, -1], [-1, 2]]
    number_test_eigenvectors = 2
    print(f'eigenvalues = {calculate_lowest_eigenvectors(test_matrix, number_test_eigenvectors)[0]}')
    print(f'eigenvectors = {calculate_lowest_eigenvectors(test_matrix, number_test_eigenvectors)[1]}')