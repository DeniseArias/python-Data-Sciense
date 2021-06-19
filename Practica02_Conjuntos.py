# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:53:00 2020

@author: DELL
"""

paises=['México','Honduras','Brasil','Honduras','Jamaica','México','Colombia','Nicaragua','Panamá','Paraguay','Brasil','Argentina','México','Brasil','Chile','Colombia','Panamá','Perú','Argentina','Uruguay']
print(len(paises))

conjunto_paises=set(paises)
print(conjunto_paises)
print(len(conjunto_paises))

conjunto_exportaciones={874,4829,3402,324,420}
print(conjunto_exportaciones)

conjunto_paises.add('Ecuador')
print(conjunto_paises)

conjunto_paises.pop()
print(conjunto_paises)

conjunto_paises.remove('Honduras')
print(conjunto_paises)

top_paises={'México','Colombia','Argentina','Costa Rica'}
diferencia=conjunto_paises.difference(top_paises)
print(diferencia)

interseccion = conjunto_paises.intersection(top_paises)
print(interseccion)

union=conjunto_paises.union(top_paises)
print(union)


a = {1, 13, 17, 19, 23, 23}

b = {19, 23, 29, 31, 37, 23}

print(a.difference(b))