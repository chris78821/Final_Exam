from read_two_column_text import read_two_column_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot
from equations_of_state import fit_eos
from generate_matrix import *
from equations_of_state import *
from convert_units import convert_units
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

if __name__ == "__main__":
    filename = 'Pt.Fm-3m.GGA-PBEsol.volumes_energies.dat'
    display_graph = 'True'

    # Fit an Equation of State
    def parse_file_name():
        filename_split = filename.split(".")[0:3]
        chemical_symbol = filename_split[0]
        crystal_symbol = filename_split[1]
        density_correlation = filename_split[2]
        return chemical_symbol, crystal_symbol, density_correlation


    # making the data to plot
    two_column_data = (read_two_column_text(filename)) / 2
    statistical_data = calculate_bivariate_statistics(two_column_data)
    quad_fit_data = calculate_quadratic_fit(two_column_data)

    # fitting the data
    fit_eos_curve, fit_eos_parameters = fit_eos(two_column_data[0], two_column_data[1],
                                                quad_fit_data, eos='birch-murnaghan')

    new_fit_curve = fit_curve_array(quad_fit_data, statistical_data[2], statistical_data[3], number_of_points=50)

    # putting data to plot into lists
    volume_array1 = convert_units(new_fit_curve[0], 'bohr/atom', 'angstrom**3/atom')
    energy_array1 = convert_units(new_fit_curve[1], 'rydberg/atom', 'eV/atom')
    volume_list1 = volume_array1.tolist()
    energy_list1 = energy_array1.tolist()
    bulk_modulus = convert_units(fit_eos_parameters[1], 'rydberg/bohr**3', 'gigapascals')

    volume_array2 = convert_units(two_column_data[0], 'bohr/atom', 'angstrom**3/atom')
    energy_list2 = convert_units(two_column_data[1], 'rydberg/atom', 'eV/atom')

    # plotting
    plt.plot(np.array(volume_array1), np.array(energy_array1), color='black')
    plt.plot(volume_array2, energy_list2, 'o', color='blue')

    x_range = max(volume_array1) - min(volume_array1)
    y_range = max(energy_array1) - min(energy_array1)
    x_limits = [min(volume_array1) - (0.1 * x_range), max(volume_array1) + (0.1 * x_range)]
    y_limits = [min(energy_array1) - (0.1 * y_range), max(energy_array1) + (0.1 * y_range)]

    plt.xlim(x_limits[0], x_limits[1])
    plt.ylim(y_limits[0], y_limits[1])
    plt.xlabel(r'$V\/(\mathrm{Å^3/atom})$')
    plt.ylabel(r'$E\/(\mathrm{eV/atom})$')

    # adding name to bottom left
    annotate_plot({'string': f"Created by Chris Thomack\n {date.today().isoformat()}",
                   'position': np.array([min(volume_array1) - 0.1, min(energy_array1) - 0.3]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # adding crystal symbol to top left
    crystal_symbol_plot = None
    if parse_file_name()[1] == 'Fm-3m':
        crystal_symbol_plot = r"$Fm\overline{3}m$"
    else:
        crystal_symbol_plot = r"$Fd\overline{3}m$"

    annotate_plot({'string': f"{crystal_symbol_plot}",
                   'position': np.array([min(volume_array1) + 0.05, max(energy_array1) - 0.13]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # adding bulk modulus to top top left
    annotate_plot({'string': f"$K_0 = {bulk_modulus:.1f}\/$GPa",
                   'position': np.array([min(volume_array1) - 0.1, max(energy_array1) + 0.1]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # adding equilibrium volume
    x_list = [volume_array1[energy_list1.index(min(energy_array1))],
              volume_array1[energy_list1.index(min(energy_array1))]]
    y_list = [min(energy_array1), y_limits[0]]
    vertical_line_y_max = min(energy_array1) - y_limits[0]
    plt.plot(x_list, y_list, 'k--')
    annotate_plot({'string': f"$V_0 = {fit_eos_parameters[3]:.2f}\/$GPa",
                   'position': np.array([volume_array1[energy_list1.index(min(energy_array1))] + 0.05,
                                         min(energy_array1) - 0.2]),
                   'alignment': ['left', 'bottom'], 'fontsize': 10})

    # add title
    plt.subplots_adjust(bottom=0.25)
    plt.title(f"{'birch-murnaghan'.capitalize()} Equation of State for "
              f"{parse_file_name()[0]} in DFT {parse_file_name()[2]}",
              y=1.1)

    if display_graph == 'True':
        plt.show()
    elif display_graph == 'False':
        plt.savefig(f"{'Thomack'}.{parse_file_name()[0]}.{parse_file_name()[1]}.{parse_file_name()[2]}."
                    f"{'birch-murnaghan'.capitalize()}.EquationOfState.png")
    else:
        exit()

    # Visualize Vectors in Space
    plt.clf()

    given_eigenfunctions = (1, 2, 3)
    matrix = generate_matrix(min(volume_array1), max(volume_array1), number_of_dimensions=100,
                             potential_name='harmonic', potential_parameter=200)
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix)
    grid = np.linspace(-10, 10, 100)
    if given_eigenfunctions[0] in eigenvectors:
        index = np.where(eigenvectors == given_eigenfunctions[0])[0]
        eigenvectors[index] = abs(eigenvectors[index])

    # make plots
    plt.plot(grid, eigenvectors[0], color='blue')
    plt.plot(grid, eigenvectors[1], color='magenta')
    plt.plot(grid, eigenvectors[2], color='green')
    plt.axhline(0, color='black')

    # set bounds
    maximum_eigenvector = max([max(abs(eigenvectors[0])), max(abs(eigenvectors[1])), max(abs(eigenvectors[2]))])
    plt.ylim(-2 * maximum_eigenvector, 2 * maximum_eigenvector)

    # create plot labels
    plt.xlabel(r"$x\/$[a.u.]")
    plt.ylabel(r"$\psi_n (x)\/$[a.u.]")
    plt.legend([fr"$\psi_1,\/E_1\/=\/{eigenvalues[0]:.3f}\/$a.u.", fr"$\psi_2,\/E_2\/=\/{eigenvalues[1]:.3f}\/$a.u.",
                fr"$\psi_3,\/E_3\/=\/{eigenvalues[2]:.3f}\/$a.u."])

    # adding name
    annotate_plot({'string': f"Created by Chris Thomack {date.today().isoformat()}",
                   'position': np.array([-10, -1.2]), 'alignment': ['left', 'bottom'], 'fontsize': 10})

    plt.title(f"Select Wavefunctions for a Harmonic Potential\n"f"on a Spatial Grid of 100 Points")

    if display_graph == 'True':
        plt.show()
    elif display_graph == 'False':
        plt.savefig(f"Thomack.{'harmonic'.capitalize()}.{given_eigenfunctions}.png")
    else:
        exit()