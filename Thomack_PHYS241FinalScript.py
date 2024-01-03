from read_two_column_text import read_two_column_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot
from equations_of_state import fit_eos
from generate_matrix import *
from generate_matrix import *
from equations_of_state import *
from convert_units import convert_units
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

__author__ = 'Chris Thomack'

def parse_file_name(filename):
    filename_split = filename.split(".")[0:3]
    chemical_symbol = filename_split[0]
    crystal_symbol = filename_split[1]
    density_correlation = filename_split[2]
    return chemical_symbol, crystal_symbol, density_correlation

if __name__ == "__main__":
    filename = 'Pt.Fm-3m.GGA-PBEsol.volumes_energies.dat'
    display_graph = 'True'

    # Fit an Equation of State
    chemical_symbol, crystal_symbol, density_correlation = parse_file_name(filename)

    # making the data to plot
    two_column_data = read_two_column_text(filename) / 2
    statistical_data = calculate_bivariate_statistics(two_column_data)
    quad_fit_data = calculate_quadratic_fit(two_column_data)

    # fitting the data
    fit_eos_curve, fit_eos_parameters = fit_eos(two_column_data[0], two_column_data[1],
                                                quad_fit_data, eos='birch-murnaghan')

    new_fit_curve = fit_curve_array(quad_fit_data, statistical_data[2], statistical_data[3], number_of_points=50)

    # converting data to plot into lists
    volume_array1 = convert_units(new_fit_curve[0], 'bohr/atom', 'angstrom**3/atom')
    energy_array1 = convert_units(new_fit_curve[1], 'rydberg/atom', 'eV/atom')

    volume_array2 = convert_units(two_column_data[0], 'bohr/atom', 'angstrom**3/atom')
    energy_list2 = convert_units(two_column_data[1], 'rydberg/atom', 'eV/atom')

    # plotting
    fig, ax = plt.subplots()
    ax.plot(volume_array1, energy_array1, color='black')  # Plotting the fit curve
    ax.plot(volume_array2, energy_list2, 'o', color='blue')  # Plotting the data points

    # Setting the axes limits
    x_range = max(volume_array1) - min(volume_array1)
    y_range = max(energy_array1) - min(energy_array1)
    ax.set_xlim(min(volume_array1) - 0.1 * x_range, max(volume_array1) + 0.1 * x_range)
    ax.set_ylim(min(energy_array1) - 0.1 * y_range, max(energy_array1) + 0.1 * y_range)

    # Adding labels
    ax.set_xlabel(r'$V\/(\mathrm{Å^3/atom})$')
    ax.set_ylabel(r'$E\/(\mathrm{eV/atom})$')

    # Preparing and applying annotations
    bulk_modulus = convert_units(fit_eos_parameters[1], 'rydberg/bohr**3', 'gigapascals')
    annotations = {
        'chemical_symbol': chemical_symbol,
        'crystal_symmetry': crystal_symbol,
        'bulk_modulus': f"{bulk_modulus:.1f} GPa",
        'equilibrium_volume_value': fit_eos_parameters[0],  # Store the numerical value without units
        'equilibrium_volume_units': 'Å³/atom',  # Include units separately
        'creator': f"Created by Chris Thomack\n{date.today().isoformat()}"
    }
    annotate_plot(ax, annotations)

    # Show or save the plot
    if display_graph == 'True':
        plt.show()
    elif display_graph == 'False':
        plt.savefig(f"{chemical_symbol}.{crystal_symbol}.{density_correlation}.EquationOfState.png")
    else:
        exit()
    # Visualize Vectors in Space
    plt.clf()
    matrix = generate_matrix(min(volume_array1), max(volume_array1), number_of_dimensions=100,
                             potential_name='harmonic', potential_parameter=200)
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix)
    number_test_eigenvectors = eigenvectors.shape[1]  # Determine the number of available eigenvectors

    grid = np.linspace(-10, 10, 100)

    # make plots
    ax2 = plt.figure().gca()
    colors = ['blue', 'magenta', 'green']  # Add more colors if needed
    for i in range(number_test_eigenvectors):
        ax2.plot(grid, eigenvectors[:, i], color=colors[i],
                 label=fr"$\psi_{i + 1},\/E_{i + 1}\/=\/{eigenvalues[i]:.3f}\/$a.u.")

    ax2.axhline(0, color='black')

    # set bounds
    maximum_eigenvector = np.max(np.abs(eigenvectors))
    ax2.set_ylim(-2 * maximum_eigenvector, 2 * maximum_eigenvector)

    # create plot labels
    ax2.set_xlabel(r"$x\/$[a.u.]")
    ax2.set_ylabel(r"$\psi_n (x)\/$[a.u.]")
    ax2.legend()

    # Annotate the second plot
    annotations_space = {
        'chemical_symbol': chemical_symbol,
        'crystal_symmetry': crystal_symbol,
        'bulk_modulus': f"{bulk_modulus:.1f} GPa",
        'equilibrium_volume_value': fit_eos_parameters[0],
        'equilibrium_volume_units': 'Å³/atom',
        'creator': f"Created by Chris Thomack\n{date.today().isoformat()}"
    }
    annotate_plot(ax2, annotations_space)

    plt.title(f"Select Wavefunctions for a Harmonic Potential on a Spatial Grid of 100 Points")

    # Show or save the second plot
    if display_graph == 'True':
        plt.show()
    elif display_graph == 'False':
        plt.savefig(f"Thomack.Harmonic.{number_test_eigenvectors}.png")
    else:
        exit()
