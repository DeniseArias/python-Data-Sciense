# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:30:40 2020

@author: DELL
"""

def agregar():
    exp2019=[3274,1325,2254,7784,425,165,7784,6555]
    exportaciones = int(input("Ingresa las exportaciones realizadas: "))
    exp2019.append(exportaciones)
    exp2019.sort(reverse=True)
    print(exp2019)
    
def multiplicar():
    print(6*5)
    
agregar()
multiplicar()