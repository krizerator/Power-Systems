import sys
import tkinter
from tkinter import filedialog as fd
import numpy as np
import pandas as pd

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
    # try:
    data = pd.ExcelFile(excel_file)
    # except ValueError:
    #     counter = 0
    #     while ".xlsx" not in excel_file and counter <= 2:
    #         new_input = input(
    #             "Error: The input file must have '.xlsx' extension. "
    #             + "Please try again.\n"
    #             )
    #         excel_file = new_input
    #         counter += 1
    #         if counter > 2:
    #             print("Limit number of retries exceeded.")
    #             sys.exit()
    #         else:
    #             continue
    #     data = pd.ExcelFile(excel_file)
    contents = ['Basis', 'Buses', 'Lines', 'Transformers',
                'Loads', 'Capacitors', 'Generators']
    vector = []
    for item, position in enumerate(contents):
        try:
            # print(item, position)
            vector.append(data.parse(contents[item]))
            # print(vector)
        except ValueError:
            print(f"ValueError: Expected DataFrame {contents[item]} not found")
            sys.exit()
    # print(vector)
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
    # print(matrices)
    return matrices

def generic_powers(voltages, angles, conductances, susceptances):
    """
    Returns two functions previously filled with the corresponding values for active
    and reactive powers for Newton Raphson method.

    Parameters:
    -----------
    voltages: array
        Corresponding bus voltages connected through lines with the desired bus.
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
    V, theta = 1, 0
    G, B = 0
    active_power = 0
    active_powers = []
    reactive_power = 0
    reactive_powers = []
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

def generic_jacobian(voltages, angles, conductances, susceptances):
    """
    Returns the jacobian for a power system filled with the corresponding values
    for the partial derivatives.

    Parameters:
    -----------
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

def iterative(voltages, angles, Jacobian, active_powers, reactive_powers, tolerance):
    """
    Returns the approximate value for a Newton Raphson power flow solution.

    Parameters:
    -----------
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
for i, element in enumerate(power_system):
    print(power_system[f"{element}"])
print(dataframes)
# print(np.cos(3.14))
