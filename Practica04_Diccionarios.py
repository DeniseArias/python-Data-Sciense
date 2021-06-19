# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:48:38 2020

@author: DELL
"""

lista_exportaciones=[3274,1325,2254,534,6954,7784,8414,7784,425,165,7784,555]
exportaciones={"Enero":3274,"Febrero":1325,"Marzo":2254,"Abril":534,"Mayo":6954,"Junio":7784,"Julio":8414,"Agosto":7784,"Septiembre":425,"Octubre":165,"Noviembre":7784}
print(exportaciones["Marzo"])
exportaciones["Diciembre"]=6555
print(exportaciones)
del(exportaciones["Enero"])
exportaciones["Abril"]=8732
print(exportaciones)

exportaciones[2018]=[520,630,120]
print(exportaciones)
print(exportaciones[2018])



exportaciones=[
{"Enero":3274,"Febrero":1325,"Marzo":2254},
{"Enero":210,"Febrero":610,"Marzo":120},
{"Enero":420,"Febrero":223,"Marzo":985},
{"Enero":590,"Febrero":3432,"Marzo":763}
]


"""
exportaciones.append(exp2019)
exportaciones.append(exp2018)
exportaciones.append(exp2017)
exportaciones.append(exp2016)
"""

print(exportaciones[0])
print(exportaciones[1]["Marzo"])


datos=[("Enero", 650),("Febrero",420),("Marzo",510)]
datos_meses=dict(datos)
print(datos_meses)

























