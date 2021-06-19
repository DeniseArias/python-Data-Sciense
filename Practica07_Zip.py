# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:33:24 2020

@author: DELL
"""
paises=("México","Canada","China","Japon")
importaciones=(430,560,310,530)
exportaciones=(1932,3540,4800,530)

agrupacion=zip(paises,importaciones,exportaciones)
print(agrupacion)
#print(list(agrupacion))#lista
#print(tuple(agrupacion))#tuplas
#print(set(agrupacion))#conjunto
print(dict(zip(paises,exportaciones)))
#Se termina la agrupacion en cuanto no existe pareja
print (list(zip(*paises)))

for pais,exportacion in zip(paises,exportaciones):
    print (pais,exportacion)
