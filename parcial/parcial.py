"""
----------------------------------------------------------------
Universidad de Costa Rica
Escuela de Ingeniería Eléctrica

Sistemas de Potencia I

    I Parcial
    ---------
    Implementación del algoritmo de Newton Raphson completo para
    determinar los flujos de potencia de un sistema genérico

Marcelo Leandro Calvo, B43730
Gabriel Libreros Chaves, B23685
Esteban Rodríguez Avilés, B76422
Eduardo Soto Obando, B77573

Prof. Dr. Andrés Arguello Guillén, Ing.
----------------------------------------------------------------
Este código se encarga de extraer datos de un archivo .xlsx.,
determina una expresión para las potencias activa P y reactiva Q
así como para el Jacobiano. Crea la matriz de admitancias para
el sistema asignado, identifica el tipo de barra y realiza las
iteraciones necesarias para resolver el problema de flujo de
potencia basándose en un valor de tolerancia establecido.
"""

import pandas as pd
import numpy as np
from multiprocessing import Pool
from power-systems import power_flow

# ------------------------------------------------------------ #
# Creación de DataFrames a partir de un archivo en formato .xlsx
# indicado por el usuario para cada pestaña

datos = pd.ExcelFile('IEEE 39 bus.xlsx')

# Separación de los datos de cada hoja en DataFrames
# If values:
base = datos.parse('Basis')
barras = datos.parse('Buses') # Solo para identificar prácticamente
lineas = datos.parse('Lines')
trafos = datos.parse('Transformers')
cargas = datos.parse('Loads')
capacitores = datos.parse('Capacitors')
generadores = datos.parse('Generators')

# def parse_to_dataframe(pd.ExcelFile df):
#     contents = ['Basis', 'Buses', 'Lines', 'Transformers',
#                 'Loads', 'Capacitors', 'Generators']
#     if(df.parse('a')):
#         print(0)
# ------------------------------------------------------------ #
# Create matrices
matrizBaseI = base.values
matrizBarrasI = barras.values # Seems like it's not useful
matrizLineasI = lineas.values
matrizTrafosI = trafos.values
matrizCargasI = cargas.values
matrizGeneradoresI = generadores.values

# Slice corresponding rows & columns if values: (Buses)
# print("Cálculo de flujos de potencia a través del método Newton-Raphson\n")
# print("Para el sistema:\n", barras.to_string(index=False))
print(barras)
print(matrizBarrasI)

# print(np.transpose(np.delete(matrizBarrasI, [0, 1])))

a_variablegenerica1 = matrizBaseI[0, 0]

b = 1/a_variablegenerica1

for i in range(0, 17):
    matrizCargas = b * matrizCargasI[i, 1:3]
    # print(matrizCargas)
# print(matrizCargasI[0][0])

# Secuencia:
#   1. Extraer datos del .xslx. y verificar
#       a. Contar líneas de una vez
#   2. Determinar una expresión para P, Q y J
#   3. Armar Y
#   4. Identificar tipos de barras
#   5. Separar expresiones explícitas e implícitas
#   6. Realizar iteraciones:
#       a. Flat start (V=1 y theta=0)
#       b. Determinar P y Q
#       c. Calcular el Jacobiano
#           i. J = LU
#           ii. LU*delta_X = -f
#               o LU*delta_v_theta = -P_Q
#           iii. Resolver para y, solver de sistemas de
#               ecuaciones lineales con Ly = -f
#           iv. Resolver para delta_x con U*delta_x = y
#       d. Hallar theta y V siguientes, x_(k+1) = x_(k) + dlta_x
#       e. Calcular el mismatch

# excel = power_flow.open_file()
# dataframes = power_flow.parse_to_dataframe(excel)
# matrices_with_contents = power_flow.generate_matrices(dataframes)
# print(matrices_with_contents[0][0][0])
