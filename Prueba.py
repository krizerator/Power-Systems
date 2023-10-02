# -*- coding: utf-8 -*-
"""
Código para el primer parcial de sistemas de potencia
"""
# Primero se importa la librería pandas
import pandas as pd


# Así como la librería numpy
import numpy as np


# Luego se crea una variable en la que se leerá el archivo 'IEEE 39 bus.xlsx'
datos = pd.ExcelFile('IEEE 39 bus.xlsx')



#Porteriormente, se hacen estructuras bidimensionales para cada hoja del archivo
# .xlsx
base = datos.parse('Basis')
barras = datos.parse('Buses')
lineas = datos.parse('Lines')
trafos = datos.parse('Transformers')
cargas = datos.parse('Loads')
capacitores = datos.parse('Capacitors')
generadores = datos.parse('Generators')

# Ahora se crean matrices a partir de las estructuras bidimensionales.
matrizBaseI = base.values  #Matriz con el valor de base de potencia
matrizBarrasI = barras.values # Matriz con la información PV, PQ y Osc para cada barra
matrizLineasI = lineas.values # Matriz con la información de las impedancias de las líneas
matrizTrafosI = trafos.values # Matriz con la información de las impedancias y taps para los trafos
matrizCargasI = cargas.values # Matriz con la información de las potencias de las cargas
matrizCapacitorI = capacitores.values # Matriz con la información de los capacitores
matrizGeneradoresI = generadores.values # Matriz con la información de los generadores

# Se determina un factor para la generación de valores de potencia en pu
# Tomando como base el valor guardado en la matriz base

a_variablegenerica1 = matrizBaseI[0, 0] # Se extrae el valor de la entrada
b = 1/a_variablegenerica1 # Y se determina su valor de factor, el cual es inverso a su valor

# Posteriormente, se utiliza este factor para dejar las cargas en pu
for i in range(0, 17):
    matrizCargas = b * matrizCargasI[i, 1:3]
    #print(matrizCargas) # Dicha matriz 17 x 2
    
#Luego se hace similar para la matriz de capacitores.
for i in range(0, 2):
    matrizCapacitor = b * matrizCapacitorI[i, 1]
    #print(matrizCapacitor) # Dicha matriz es 2 x 1

# Luego, se convierten a pu la potencia generada por los generadores
for i in range(0, 9):
    matrizPotenciaGenerada = b * matrizGeneradoresI[i, 2:4]
    #print(matrizPotenciaGenerada) #Dicha matriz es 2 x 9

# Se crea la matriz de impedancias del transformador
for i in range(0, 12):
    realT = matrizTrafosI[i, 2:3]
    imaginarioT = 1j*matrizTrafosI[i, 3:4]
    matrizIT = realT + imaginarioT # Aquí la matrizIT tiene un número complejo de impedancia
    #print(matrizIT)
'''OJO, PROBLEMA 1: No entiendo porque dentro del for anterior me imprime toda la matriz
y en el siguiente print solo me imprime el último valor '''
#print(matrizIT)

# Se crea un arreglo con los valos del a'(o sea, la relación con el tap) que se usará para calcular el A, B y C del 
# modelo del transformador.
for i in range(0, 12):
    tapBus1 = matrizTrafosI[i, 5:6]
    #print(tapBus1)


'''PROBLEMA 2: A partir de aquí lo que quiero es intentar pasar estos valores de impedancias a valores de 
admitancias para poder calcular el A, B y C del modelo para el Trafo, pero no puedo obtener los valores
 de las entradas de la matrizIT, como se observa al correr el código'''
 
 
# Una vez creada la matriz de impedancias del transformador, se procede a calcular
# las admitancias A, B y C.



    

 


