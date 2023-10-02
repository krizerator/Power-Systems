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
            print(item, position)
            vector.append(data.parse(contents[item]))
            print(vector)
        except ValueError:
            print(f"ValueError: Expected DataFrame {contents[item]} not found")
            sys.exit()
    print(vector)
    return vector

def generate_matrices(vector):
    """
    Converts a set of DataFrames into individual matrices.

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

print(
    """
    Por favor seleccione el archivo de excel al cual desea aplicar el método de
    Newton Raphson.
    """
    )
input("Presione enter para continuar.")
excel = open_file()
dataframes = parse_to_dataframe(excel)
# matrices_with_contents = generate_matrices(dataframes)
# print(matrices_with_contents)
# apparent_power = matrices_with_contents[0][0][0]
# print(apparent_power)
# power_system = {
#     "basis" : contents[0][0][0],
#     "buses" : contents[1][0],
#     "lines" : contents[0],
#     "transformers" : contents[0],
#     "loads" : contents[0],
#     "capacitors" : contents[0],
#     "generators" : contents[0]
#     }
# print(power_system)

# np.delete(contents, 0, 0)
# print(np.cos(3.14))
