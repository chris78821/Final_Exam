__author__ =  'Chris Thomack'

import numpy as np

from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from lowest_eigenvectors import lowest_eigenvectors
from bivariate_statistics import bivariate_statistics
from two_column_text_read import two_column_text_read



# Part 1: Read in two columns of data from a text file of arbitrary length
data = two_column_text_read('dataset.txt')
print('[1] input data shape: {} => return type: {}'.format(data.shape, type(data)))


# Part 2: Calculate statistical characteristics of a data set 
# using SciPy's stats.describe
statistics = bivariate_statistics(data)
# Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value  
print('[2] Statistics => return type: {} shape: {}'.format(
    type(statistics), 
    statistics.shape
))
# Pretty print the statistics
print('[2] Mean of y: {:.2f}'.format(statistics[0]))
print('[2] Standard deviation of y: {:.5f}'.format(statistics[1]))
print('[2] Minimum x-value: {:.4f}'.format(statistics[2]))
print('[2] Maximum x-value: {:.4f}'.format(statistics[3]))
print('[2] Minimum y-value: {:.4f}'.format(statistics[4]))
print('[2] Maximum y-value: {:.4f}'.format(statistics[5]))

# Part 3: Fit a quadratic polynomial to a two row NumPy array 
# of x-y data using NumPy's polynomial package
coefficients = quadratic_fit(data)
print('[3] Quadratic polynomial coefficients => return type: {} shape: {}'.format(
    type(coefficients), 
    coefficients.shape
))
# Pretty print the coefficients
print('[3] Quadratic term: {:.6f}'.format(coefficients[0]))
print('[3] Linear term: {:.6f}'.format(coefficients[1]))
print('[3] Constant term: {:.6f}'.format(coefficients[2]))

# Part 4: Make fit curve using fit polynomial coefficients, NumPy's 
# polynomial package, and minimum and maximum x-values
x_min = statistics[2]
x_max = statistics[3]
fit_curve = fit_curve_array(coefficients, x_min, x_max, 100)
print('[4] Fit curve => return type: {} shape: {}'.format(type(fit_curve), fit_curve.shape))

# Part 5: Create a combined scatter and curve plot for the data and the fit polynomial, 
# respectively, using Matplotlib pyplot's plot function
charts = plot_data_with_fit(data, fit_curve, data_format='o', fit_format='r-')
print('[5] Plot return type: {}'.format(type(charts[0])))

# Part 6: Identify eigenvectors with smallest K eigenvalues 
# given input matrix using NumPy's eigfunction
matrix = np.array([
    [2,-1,0,0,0,0,0,0,0,0],
    [-1,2,-1,0,0,0,0,0,0,0],
    [0,-1,2,-1,0,0,0,0,0,0],
    [0,0,-1,2,-1,0,0,0,0,0],
    [0,0,0,-1,2,-1,0,0,0,0],
    [0,0,0,0,-1,2,-1,0,0,0],
    [0,0,0,0,0,-1,2,-1,0,0],
    [0,0,0,0,0,0,-1,2,-1,0],
    [0,0,0,0,0,0,0,-1,2,-1],
    [0,0,0,0,0,0,0,0,-1,2]
])
lowest_eig = lowest_eigenvectors(matrix, 3)
eigenvalues, eigenvectors = lowest_eig
print('[6] Eigenvalues => return type: {} shape: {} => {}'.format(
    type(eigenvalues),
    eigenvalues.shape,
    eigenvalues
))
print('[6] Eigenvectors => return type: {} shape: {} => \n{}'.format(
    type(eigenvectors),
    eigenvectors.shape,
    eigenvectors
))

