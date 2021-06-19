#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:57:23 2020

@author: DELL
"""
archivo = open("informacion.txt","r") # read/ modo lectura
#open("informacion.txt","w") # write/ Modo sobreescribir
#open("informacion.txt","a") # apend/ modo Agregar al existente

"""
#contenido = archivo.read()
contenido = archivo.readline() #ejecutarla tantas veces hasta encontar lo buscado
print(contenido)


for linea in archivo:
    print(linea)
"""

lista_contenido = archivo.readlines()
print(lista_contenido)

archivo.close()

escribir_archivo = open("archivo_escritura.txt","w")
escribir_archivo.write("Exportaciones realizadas por pais: \n")
"""
for elemento in lista_contenido:
    escribir_archivo.write(elemento)
"""
escribir_archivo.writelines(lista_contenido)
escribir_archivo.close()

escribir_archivo = open("archivo_escritura.txt","a")
nuevo_dato=input("Ingresa nueva información: ")
escribir_archivo.write(nuevo_dato)
escribir_archivo.close()

