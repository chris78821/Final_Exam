""" We want a definition statement that inputs a file and outputs two columns"""

__author__ = "Chris Thomack"

import numpy as np


def read_two_column_text(file_name):
    try:
        data = open(file_name, 'r')
    except OSError:
        print(OSError)
        return

    data_contents = data.readlines()
    data.close()
    data_list_one = []
    data_list_two = []
    for line in data_contents:
        column_one = float(line.split()[0])
        data_list_one.append(column_one)
    for line in data_contents:
        column_two = float(line.split()[1])
        data_list_two.append(column_two)
    data_array = np.array([data_list_one, data_list_two])
    return data_array


if __name__ == "__main__":
    file = 'volume_energies'
    test_data = read_two_column_text(file)
    print(f'data={test_data}, shape={test_data.shape}')