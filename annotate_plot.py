import matplotlib.pyplot as plt
import numpy as np
from datetime import date

__author__ = 'Chris Thomack'

def annotate_plot(ax, annotations):
    """
    Annotate the plot with specific information based on structured data.

    Parameters:
    ax (matplotlib.axes.Axes): The axes object to annotate.
    annotations (dict): A structured dictionary containing the annotation details.

    Returns:
    None
    """
    # Annotate chemical symbol in the upper left corner
    ax.text(0.05, 0.95, annotations['chemical_symbol'], transform=ax.transAxes,
            horizontalalignment='left', verticalalignment='top', fontsize=12)

    # Annotate crystal symmetry symbol centered above the curve in italic font
    ax.text(0.5, 0.8, annotations['crystal_symmetry'], transform=ax.transAxes,
            horizontalalignment='center', verticalalignment='center', fontsize=12, style='italic')

    # Annotate bulk modulus above the crystal symmetry symbol
    ax.text(0.5, 0.75, annotations['bulk_modulus'], transform=ax.transAxes,
            horizontalalignment='center', verticalalignment='center', fontsize=12)

    # Annotate equilibrium volume with units
    # To this line
    equilibrium_volume_str = f"{annotations['equilibrium_volume_value']:.2f} {annotations['equilibrium_volume_units']}"

    ax.axvline(x=annotations['equilibrium_volume_value'], color='black', linestyle='dashed')
    ax.text(annotations['equilibrium_volume_value'], ax.get_ylim()[0] + (ax.get_ylim()[1] - ax.get_ylim()[0]) / 10,
            equilibrium_volume_str, fontsize=12, color='black', verticalalignment='bottom')

    # Annotate with the creator's signature and current date in the bottom left
    ax.text(0.05, 0.01, annotations['creator'],
            transform=ax.transAxes, horizontalalignment='left', verticalalignment='bottom', fontsize=10)

# Example plot data
volume_array1 = np.linspace(1, 10, 100)
energy_array1 = volume_array1 ** 2  # Example quadratic relationship

# Create the plot
fig, ax = plt.subplots()
ax.plot(volume_array1, energy_array1, color='black')  # Example fit curve
ax.plot(volume_array1, energy_array1 + 10, 'o', color='blue')  # Example data points

# Preparing and applying annotations
annotations = {
    'chemical_symbol': 'Pt',
    'crystal_symmetry': 'Fm-3m',
    'bulk_modulus': "K₀ = 200 GPa",  # Example bulk modulus value
    'equilibrium_volume_value': 5.00,  # Example equilibrium volume value (numerical value only)
    'equilibrium_volume_units': "Å³/atom",  # Example units for equilibrium volume
    'creator': "Created by Chris Thomack\n" + date.today().isoformat()
}


# Annotate the plot
annotate_plot(ax, annotations)
