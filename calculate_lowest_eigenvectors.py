"""
Calculates lowest eigenvector and eigenvalue of a matrix.
"""

__author__ = 'Chris Thomack'

import numpy as np

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """
    Calculate the lowest eigenvalues and their corresponding eigenvectors.

    :param square_matrix: The square matrix for which eigenvalues and eigenvectors are calculated.
    :param number_of_eigenvectors: The number of lowest eigenvalues and eigenvectors to compute.
    :return: Tuple containing lowest eigenvalues and their corresponding eigenvectors.
    """
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    # Sort eigenvalues and eigenvectors in ascending order
    sorted_indices = np.argsort(eigenvalues)
    lowest_eigenvalues = eigenvalues[sorted_indices[:number_of_eigenvectors]]
    lowest_eigenvectors = eigenvectors[:, sorted_indices[:number_of_eigenvectors]]
    return lowest_eigenvalues, lowest_eigenvectors

if __name__ == "__main__":
    test_matrix = np.array([[2, -1], [-1, 2]])
    number_test_eigenvectors = 3  # You can change this to the number of lowest eigenvectors you want
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(test_matrix, number_test_eigenvectors)
    print(f'Lowest eigenvalues = {eigenvalues}')
    print(f'Corresponding eigenvectors = {eigenvectors}')
