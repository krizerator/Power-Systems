'''
                    Universidad de Costa Rica
                      Facultad de Ingeniería
                 Escuela de Ingeniería Eléctrica
                             IE-0365 
                    Transmisión de Potencia

                  ARONAF_ESTEBANRA_PROYECTO2.py

Autores: Aron Alvarado Fonseca B80317 <aron.alvarado@ucr.ac.cr>
         Esteban Rodríguez Avilés B76422 <estebanalonso.rodriguez@ucr.ac.cr>

Fecha: 05/07/2023

Descripción: contiene un programa que recibe los datos de un sistema de potencia 
de un archivo llamado "System_data.xlsx", y calcula en estado estacionario: 
la corriente de falla en pu y kA; la corriente por todos los elementos en pu y 
kA; y las tensiones de falla en pu y kV para una falla trifásica a tierra,
monofásica a tierra, bifásica (fase-fase) y bifásica a tierra en la barra 7 con
una impedancia de falla de 10 ohms. Dichos resultados se exportan en un archivo 
llamdo "resultados.txt".

Nota: Ambos autores asumimos el 100% de la responsabilidad por el código reali_
zado.
 
'''

# Se importan las librerías pandas y numpy

import pandas as pd

import numpy as np

# Se lee el archivo 'IEEE 39 bus.xlsx' que contiene los datos del sistema

datos_sis = pd.ExcelFile('IEEE 39 bus.xlsx')

# Se asigna la información de la hoja 'Generators' en un dataframe llamado da_
# tos _gen


# Se asigna la información de la hoja 'Basis' en un dataframe llamado da_
# tos _base
datos_base = datos_sis.parse('Basis')



# Se asigna la información de la hoja 'Buses' en un dataframe llamado da_
# tos _buse
datos_buses = datos_sis.parse('Buses')



# Se asigna la información de la hoja 'Lines' en un dataframe llamado da_
# tos _lines
datos_lines = datos_sis.parse('Lines')



# Se asigna la información de la hoja 'Transformers' en un dataframe llamado da_
# tos_trans
datos_trans = datos_sis.parse('Transformers')



# Se asigna la información de la hoja 'Loads' en un dataframe llamado da_
# tos_load
datos_load = datos_sis.parse('Loads')


# Se asigna la información de la hoja 'Capacitors' en un dataframe llamado da_
# tos_capi
datos_capi = datos_sis.parse('Capacitors')


# Se asigna la información de la hoja 'Generators' en un dataframe llamado da_
# tos_gen
datos_gen = datos_sis.parse('Generators')
