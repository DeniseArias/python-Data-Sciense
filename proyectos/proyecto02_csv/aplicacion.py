# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:40:01 2020

@author: DELL
"""

import csv
with open("exportaciones2020.csv","r") as archivo_csv:
    #lector=csv.reader(archivo_csv, delimiter=",")
    lector = csv.DictReader(archivo_csv)
    for linea in lector:
       print(linea)
    
info=[
      ("Mexico","cars"),
      ("Canada","petroleum"),
      ("United States","planes"),
      ("China","electronic"),
      ("South Korea","computers"),
      ("Germany","cars")
      ]
with open("Info_exp.csv","w") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerows(info)
    

paises=[
    {"pais":"México","fecha":2019, "exp":(4930,2045,4836)},
    {"pais":"Canadá","fecha":2019, "exp":(4782,6984,47059,7365)},
    {"pais":"Brasil","fecha":2018, "exp":(85704,74632)},
    {"pais":"China","fecha":2019, "exp":(4730,48526,6934,12820)},
    {"pais":"Japón","fecha":2018, "exp":(19314,4183,4580,4750)}
]

with open("Dict_exp.csv","w") as archivo_dict:
    campos=["fecha","pais","exp"]
    escritor= csv.DictWriter(archivo_dict,fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(paises)
