import sys
import tkinter
from tkinter import filedialog as fd
import sympy as sp
import numpy as np
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)

def open_file():
    """
    Opens a specified .xlsx file through a dialog box.

    Returns
    -------
    str
        A string containing the filepath for the selected file.
    """
    tkinter.Tk().withdraw()
    filepath = fd.askopenfilename(title="Select a file",
                                          filetypes=[("Excel files", "*.xlsx")])
    print(f"La ruta del archivo seleccionado es: {filepath}")
    return filepath

def parse_to_dataframe(excel_file):
    """
    Parses an excel file into several dataframes to extract contents related to
    buses, lines, transformers, loads and generators for power systems.

    Parameters
    ----------
    excel_file : str
        Contents of a .xlsx file with information related to power flow cases.

    Returns
    -------
    Array of DataFrames
        An array containing a set of DataFrames taken from the spreadsheet.
    """
    data = pd.ExcelFile(excel_file)
    contents = ['Basis', 'Buses', 'Lines', 'Transformers',
                'Loads', 'Capacitors', 'Generators']
    vector = []
    for item, position in enumerate(contents):
        try:
            vector.append(data.parse(contents[item]))
        except ValueError:
            print(f"ValueError: Expected DataFrame {contents[item]} not found")
            sys.exit()
    return vector

def generate_matrices(vector):
    """
    Converts an array of DataFrames into individual matrices.

    Parameters
    ----------
    vector: array
        Contains a set of DataFrames that will be converted to matrices.

    Returns
    -------
    matrices
        Matrices for each of the DataFrames contained in vector.
    """
    matrices = []
    for index, position in enumerate(vector):
        matrices.append(vector[index].values)
    return matrices

def add_lines_items_to_matrix(matrix, system):
    """
    Returns the matrix with modified values based on lines data from the power
    system.

    Parameters
    ----------
    matrix: matrix
        Matrix to be filled with line impedance values.
    data: array
        Array that contains information about the lines admittances.

    Returns
    -------
    matrix
        Matrix with modified impedance entries.
    """
    lines_data = system['lines']
    buses_data = system['buses']
    for index, position in enumerate(lines_data):
        bus_1 = int(lines_data[index][0])
        bus_2 = int(lines_data[index][1])
        impedance = complex(lines_data[index][2],lines_data[index][3])
        susceptance = complex(0,lines_data[index][4])
        admittance = 1/impedance + susceptance/2
        matrix[bus_1-1][bus_2-1] -= admittance
        matrix[bus_2-1][bus_1-1] -= admittance
        matrix[bus_1-1][bus_1-1] += admittance
        matrix[bus_2-1][bus_2-1] += admittance
    # for index, position in enumerate(lines_data):
    #     line = int(lines_data[index][0])
    #     for sub_index, position in enumerate(buses_data):
    #         if line-1 < sub_index and matrix[line-1][index] != 0 and line-1 != sub_index:
    #             matrix[line-1][line-1] += matrix[line-1][index]
    #             print(f"Data added to Y{line}{line}: ", matrix[line-1][line-1])
    #         else:
    #             print(f"No data added to Y{line}{line} for i-j:{line}-{sub_index+1}")
    #             continue
    print(matrix)
    return matrix

def add_transformers_items_to_matrix(matrix, data):
    """
    a
    """
    for index, position in enumerate(data):
        bus_1 = int(data[index][0])
        bus_2 = int(data[index][1])
        impedance = complex(data[index][2],data[index][3])
        admittance_cc = 1/impedance
        bus_tap = data[index][5]
        parameter_A = admittance_cc/bus_tap
        parameter_B = admittance_cc/bus_tap*(1/bus_tap-1)
        parameter_C = admittance_cc*(bus_tap-1)/bus_tap
        admittance = parameter_A + (parameter_B + parameter_C)/2
        matrix[bus_1-1][bus_2-1] = matrix[bus_1-1][bus_2-1] + admittance
        matrix[bus_2-1][bus_1-1] = matrix[bus_2-1][bus_1-1] + admittance
    return matrix

def admittance_matrix(system):
    """
    Returns the admittance matrix for a power system.

    Parameters
    ----------
    power_system: dict
        Dictionary containing data necessary to determine the admittance matrix for
        a power syste.

    Returns
    -------
    matrix
        The admittance matrix for the specified power system
    """
    buses = system['buses']
    transformers = system['transformers']
    matrix = np.zeros(shape=(len(buses), len(buses)), dtype=np.complex_)
    matrix = add_lines_items_to_matrix(matrix, power_system)
    matrix = add_transformers_items_to_matrix(matrix, transformers)
    return matrix

def vector_index():
    """
    Returns a vector for voltages and angles of a power system for a Newton Raphson
    iteration.

    Parameters
    ----------
    s
    """
    return

def generic_powers(system, voltages, angles):
    """
    Returns two functions previously filled with the corresponding values for active
    and reactive powers for Newton Raphson method.

    Parameters
    ----------
    power_system: dict
        Dictionary containing data related to parameters needed to calculate powers.
    """
    active_power = 0
    active_powers = []
    reactive_power = 0
    reactive_powers = []
    buses = system['buses']
    matrix = np.zeros(shape=(len(buses), len(buses)), dtype=np.complex_)
    bars = len(voltages)
    for p_index, position in bars:
        for p_sub_index, sub_position in bars:
            active_power = active_power + (
                V[p_index]*V[p_sub_index]*(
                    G[p_index][p_sub_index]*np.cos(theta[p_index][p_sub_index]) + (
                    B[p_index][p_sub_index]*np.sin(theta[p_index][p_sub_index]))))
            if p_sub_index == bars:
                active_powers.append(active_power)
                active_power = 0
            else:
                continue
    for q_index, position in bars:
        for q_sub_index, sub_position in bars:
            reactive_power = reactive_power + (
                V[q_index]*V[q_sub_index]*(
                    G[q_index][q_sub_index]*np.cos(theta[q_index][q_sub_index]) + (
                    B[q_index][q_sub_index]*np.sin(theta[q_index][q_sub_index]))))
            if q_sub_index == bars:
                reactive_powers.append(reactive_power)
                reactive_power = 0
            else:
                continue
    return active_powers, reactive_powers

def partial_derivative(expression, respect_with, **kwargs):
    """
    
    """
    derivative = sp.Derivative(expression, respect_with).doit()
    derivative.evalf(subs={})
    return

def generic_jacobian(iteration):
    """
    Returns the jacobian for a power system filled with the corresponding values
    for the partial derivatives.

    Parameters
    ----------
    voltages: array
        Bus voltages for the power system.
    angles: array
        Angles between buses.
    conductances: array
        Conductances for the lines.
    susceptances: array
        Susceptances for the lines.
    """
    voltages = voltages
    angles = angles
    conductances = conductances
    susceptances = susceptances
    return

def iterative(iteration):
    """
    Returns the approximate value for a Newton Raphson power flow solution.

    Parameters
    ----------
    voltages: array
        Corresponding buses voltages connected through lines with the desired bus.
    angles: array
        Corresponding angles between the desired bus and each connected bus through
        a line.
    conductances: array
        Corresponding conductance for the lines connecting the desired bus with the
        rest of the buses.
    susceptances: array
        Corresponding susceptance for the lines connecting the desired bus with the
        rest of the buses.
    """
    voltages = voltages
    angles = angles
    conductances = conductances
    susceptances = susceptances
    return

print(
    """
    Por favor seleccione el archivo de excel al cual desea aplicar el método de
    Newton Raphson.
    """
    )
input("Presione enter para continuar.")
excel = open_file()
dataframes = parse_to_dataframe(excel)
# print(dataframes[0], "\n", dataframes[1], "\n", dataframes[2])
matrices_with_contents = generate_matrices(dataframes)
power_system = {
    "basis" : matrices_with_contents[0][0][0],
    "buses" : matrices_with_contents[1],
    "lines" : matrices_with_contents[2],
    "transformers" : matrices_with_contents[3],
    "loads" : matrices_with_contents[4],
    "capacitors" : matrices_with_contents[5],
    "generators" : matrices_with_contents[6]
}
admittance_matrix(power_system)
# for i, element in enumerate(power_system):
    # print(power_system[f"{element}"])
# print(dataframes)
# print(np.cos(3.14))
