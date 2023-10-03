
import sys
import tkinter
from tkinter import filedialog as fd
import sympy as sp
import numpy as np
import pandas as pd

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
    try:
        data = pd.ExcelFile(excel_file)
        counter = 0
        while ".xlsx" not in excel_file and counter <= 2:
            new_input = input(
                "Error: The input file must have '.xlsx' extension. "
                + "Please try again.\n"
                )
            excel_file = new_input
            counter += 1
            if counter > 2:
                print("Limit number of retries exceeded.")
                sys.exit()
            else:
                continue
        data = pd.ExcelFile(excel_file)
    except ValueError:
        print("ValueError: the parameter must contain '.xlsx' extension")
        sys.exit()
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

parse_to_dataframe('/mnt/c/Users/luise/OneDrive/Escritorio/UCR/Sistemas de Potencia/parcial/A bus.xlx')
parse_to_dataframe('IEEE 39 bus - Copy.xlsx')
