# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:56:38 2020

@author: DELL
"""

semestre_1=[3274,1325,2254,533,6954,7784]
semestre_2=[8414,7784,425,165,7784,55]
productos_exportacion=["Computadoras","Tablets", "Teclados","Smart Wathc"]

totales=semestre_1+semestre_2
print(totales)
print(semestre_1+semestre_2)

print(totales*3)

totales[-1]=6555
print(totales)

totales[9]=2165
print(totales)

#Metodos
print(totales.count(7784))

productos_exportacion.insert(2,"Audifonos")
print(productos_exportacion)

productos_exportacion.insert(0,"Computadora")

#productos_exportacion.pop(1)
productos_exportacion.remove("Computadoras")
print(productos_exportacion)

totales.sort(reverse=True)
#totales.reverse()#Solo voletea la lista
print(totales)

productos_exportacion.sort()
print(productos_exportacion)