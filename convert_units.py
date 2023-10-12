"converts units"

__author__ =  'Chris Thomack'

import scipy as sp


def convert_units(data, current_value, new_value):
    # data in bohr per atom
    converted_value = None
    if current_value == 'bohr/atom' and new_value == 'angstrom**3/atom':
        # m/bohr
        bohr_radius = sp.constants.physical_constants['Bohr radius'][0]
        # m/angstrom
        angstrom = sp.constants.angstrom
        return_value = (data * bohr_radius ** 3) / angstrom ** 3
    elif current_value == 'rydberg/atom' and new_value == 'eV/atom':
        rydberg_conversion = sp.constants.physical_constants['Rydberg constant times hc in eV'][0]
        return_value = data * rydberg_conversion
    elif current_value == 'rydberg/bohr**3' and new_value == 'gigapascals':
        bohr_radius = sp.constants.physical_constants['Bohr radius'][0]
        rydberg_conversion = sp.constants.physical_constants['Rydberg constant times hc in J'][0]
        return_value = ((data * rydberg_conversion) / bohr_radius ** 3) * 10 ** -9

    return return_value

