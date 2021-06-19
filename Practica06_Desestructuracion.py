# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:22:19 2020

@author: DELL
"""

exportaciones=850,920
mexico,canada=exportaciones

print(mexico)
print(canada)

#Se desestructura las listas colocando cada valor en cada nueva variable
china,japon=1810,1516
colombia,chile,brasil=[520,630,450]

paises=[("México",850),("Canada",920),("China",1810)]

for nombre,total in paises:
    print(f"{nombre} realizo {total} exportaciones en 2019")
