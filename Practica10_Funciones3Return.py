# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 07:30:57 2020

@author: DELL
"""
paises=[
    {"pais":"México","fecha":2019, "exp":(4930,2045,4836)},
    {"pais":"Canadá","fecha":2019, "exp":(4782,6984,47059,7365)},
    {"pais":"Brasil","fecha":2018, "exp":(85704,74632)},
    {"pais":"China","fecha":2019, "exp":(4730,48526,6934,12820)},
    {"pais":"Japón","fecha":2018, "exp":(19314,4183,4580,4750)}
]

def promedio_exp(pais_a_calcular):
    if len(pais["exp"])==0:
        return "No hay exportaciones"
    else:
        promedio=sum(pais["exp"])/len(pais["exp"])
        return promedio

def nombre_pais(pais):
    nombre=pais["pais"]
    return nombre

def mostrar_info(pais):
    nombre=nombre_pais(pais)
    promedio = promedio_exp(pais)
    print(f"Exportaciones promedio en {nombre}:{promedio}")

        


for pais in paises:
    mostrar_info(pais)
    
    
    
 
