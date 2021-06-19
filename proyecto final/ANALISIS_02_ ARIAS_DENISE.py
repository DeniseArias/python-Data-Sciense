# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:38:13 2020

@author: DELL
""" 
import csv


with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector=csv.reader(archivo_csv)

    total_rutas=[]
    for viaje in lector:
        ruta_encontrada=0
        for ruta in total_rutas:
            if ((viaje[2]== ruta[0] or viaje[2]== ruta[1]) and (viaje[3]== ruta[0] or viaje[3]==ruta[1])):
                ruta[2]+= 1
                ruta[3]+=int(viaje[9])
                ruta_encontrada=1
                break
        if(ruta_encontrada==0):
            try:
                total_rutas.append([viaje[2],viaje[3],1,int(viaje[9])])
            except ValueError:
                continue;
    
for rutas in total_rutas:
    rutas.append(rutas[3]/rutas[2])
total_rutas.sort(key=lambda x: x[3], reverse=True)
                  
"""
#Verifcamos la opcion 2 , primeramente sacamos las frecuencias (absoluta y relativa)
#obtenemos valores y pasamos al excel, posteriormente agregamos un campo mas a las listas de 
#total viaje para obtener el promedio de viaje
#pasamos a excel y realizamos regla de 3

    frecuancia_acumulada=[]
    total_Viaje=[]

    for viaje in lector:
        viaje_encontrado=0
        for tipo_viaje in total_Viaje:
            if (viaje[7]== tipo_viaje[0]):
                tipo_viaje[1]+=int(viaje[9]) #se ocupa para obtener total numerico
                tipo_viaje[2]+=1 #se ocupa para obtener la frecuencia absoluta
                viaje_encontrado=1
                break
        if(viaje_encontrado==0):
            try:
                total_Viaje.append([viaje[7],int(viaje[9]),1])
            except ValueError:
                 continue;
            #total_Viaje.append([viaje[7],1]) #iniciamos frecuencia absoluta
            
diccionario_viajes=dict(total_Viaje)
total_Viaje.sort(key=lambda x: x[1], reverse=True)
for viaje in total_Viaje:
    viaje.append(viaje[1]/viaje[2]) #promedio por viaje
#diccionario_viajes=dict(total_Viaje)
#num_viajes=sum(diccionario_viajes.values())
#for viaje in total_Viaje:
#    viaje[1]=viaje[1]/num_viajes #frecuencia relativa
n=0
for viaje in total_Viaje:
    print(viaje[1])
    print(frecuancia_acumulada[n])
    frecuancia_acumulada.append(frecuancia_acumulada[n]+viaje[1]) #frecuencia acumulada
    n+=1
diccionario_viajes=dict(total_Viaje)
"""


"""    
#Verificamos la opcion 3
#Creamos 3 listas, las primeras 2 guardaran todos los movimientos divididos por importacion o exportacion
#Lo enviamos al metodo de rutas_demandadas, el cual se encarga de obtener por pais el total de transaccion 
#El promedio, la media y el tipo de transaccion, devolviendo una lista con los valores ordendos
#La tercer lista sera la union de las 2 anteriores y ordenaremos todas las listas por el promedio 
#de sus ganancias
    listaIm = []
    listaEx=[]
    
    for viajes in lector:
        if (viajes[1]=="Imports"):
            listaIm.append(viajes)
        elif(viajes[1]=="Exports"):
            listaEx.append(viajes)
            
import Funciones as f
importaciones=f.rutas_demandadas(listaIm,"Imports")
exportaciones=f.rutas_demandadas(listaEx,"Exports")

top10=importaciones+exportaciones
top10.sort(key=lambda x: x[2], reverse=True)
""" 



















