# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:16:45 2020

@author: DELL
"""

import csv

totales=[]

with open("exportaciones2020.csv","r") as archivo_csv:
    lector=csv.reader(archivo_csv)
    
    for linea in lector :
        if(linea[2]=="total"):
            continue
        totales.append(int(linea[2]))

print("El total de las exportaciones es: ",sum(totales))

exp_mexico=[]
with open("exportaciones2020.csv","r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for linea in lector :
        if linea["origen"]=="mexico":
            exp_mexico.append(int(linea["total"]))

print(exp_mexico)
print("Exportaciones totales de Mexico: ", sum(exp_mexico))

