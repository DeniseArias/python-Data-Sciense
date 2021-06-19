# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 22:06:01 2020

@author: DELL
"""
multiplicar = lambda a,b: a*b

print(multiplicar(6,5))

promedio = lambda secuencia:sum(secuencia)/len(secuencia)

paises=[
    {"pais":"México","fecha":2019, "exp":(4930,2045,4836)},
    {"pais":"Canadá","fecha":2019, "exp":(4782,6984,47059,7365)},
    {"pais":"Brasil","fecha":2018, "exp":(85704,74632)},
    {"pais":"China","fecha":2019, "exp":(4730,48526,6934,12820)},
    {"pais":"Japón","fecha":2018, "exp":(19314,4183,4580,4750)}
]

for pais in paises:
    print(promedio(pais["exp"]))    
    
    
def mayor_edad(datos, edad):
    return edad(datos) >= 18

usuario = { 'nombre_usuario': 'fco123', 'edad': '23' }
print(mayor_edad(usuario, lambda x: int(x['edad'])))