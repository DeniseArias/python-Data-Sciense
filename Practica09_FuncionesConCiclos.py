# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:46:43 2020

@author: DELL
"""
exp2019=[3274,1325,2254,7784,425,165,7784,6555]
def agregar(lista):
    exportaciones = int(input("Ingresa las exportaciones realizadas: "))
    lista.append(exportaciones)
    lista.sort(reverse=True)
    print(lista)
    
agregar(exp2019)
agregar([50,126,763,41,193,165])



paises=[
    {"pais":"México","fecha":2019, "exp":(4930,2045,4836)},
    {"pais":"Canadá","fecha":2019, "exp":(4782,6984,47059,7365)},
    {"pais":"Brasil","fecha":2018, "exp":(85704,74632)},
    {"pais":"China","fecha":2019, "exp":(4730,48526,6934,12820)},
    {"pais":"Japón","fecha":2018, "exp":(19314,4183,4580,4750)}
]

def promedio_exp(pais_a_calcular=paises[0], fecha_para_calcular="2019"):
    if(pais_a_calcular["fecha"]==fecha_para_calcular):
        nombre=pais_a_calcular["pais"]
        exportaciones = pais_a_calcular["exp"]
        
        promedio=sum(exportaciones)/len(exportaciones)
        
        print (f"Exportaciones promedio en {nombre}:{promedio}")

for pais in paises:
    promedio_exp(fecha_para_calcular=2019,pais_a_calcular=pais)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    