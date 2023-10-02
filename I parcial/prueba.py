# -*- coding: utf-8 -*-
"""
Código para el primer parcial de sistemas de potencia
"""
# Primero se importa la librería pandas
import pandas as pd

# Así como la librería numpy
#import numpy as np


# Luego se crea una variable en la que se leerá el archivo 'IEEE 39 bus.xlsx'
datos = pd.ExcelFile('IEEE 39 bus.xlsx')

#Porteriormente, se hacen
base = datos.parse('Basis')
print(base)
barras = datos.parse('Buses')
lineas = datos.parse('Lines')
trafos = datos.parse('Transformers')
cargas = datos.parse('Loads')
capacitores = datos.parse('Capacitors')
generadores = datos.parse('Generators')

matrizBaseI = base.values
matrizBarrasI = barras.values
matrizLineasI = lineas.values
matrizTrafosI = trafos.values
matrizCargasI = cargas.values
matrizGeneradoresI = generadores.values

print(matrizCargasI)

a_variablegenerica1 = matrizBaseI[0, 0]

b = 1/a_variablegenerica1

for i in range(0, 17):
    matrizCargas = b * matrizCargasI[i, 1:3]
    print(matrizCargas)
print(matrizCargasI[0][0])
