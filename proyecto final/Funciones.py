import statistics as s
def rutas_demandadas(lista,direccion):
    paises_agrupados=[]
    for elementos in lista:
        pais_encontrado=0
        for pais in paises_agrupados:
            if(direccion=="Imports"):
                if (pais[0]== elementos[3]):
                    pais[1]+=int(elementos[9])
                    pais[3].append(int(elementos[9]))
                    pais_encontrado=1
                    break
            elif(direccion=="Exports"):
                if (pais[0]== elementos[2]):
                    pais[1]+=int(elementos[9])
                    pais[3].append(int(elementos[9]))
                    pais_encontrado=1
                    break
        if (pais_encontrado==0 and direccion=="Imports"):
            paises_agrupados.append([elementos[3],int(elementos[9]),0,[],"Imports"])
        elif(pais_encontrado==0 and direccion=="Exports"):
            paises_agrupados.append([elementos[2],int(elementos[9]),0,[],"Exports"])
            
    for pais in paises_agrupados:
        pais[2]=s.mean(pais[3])
        pais[3]= s.median(pais[3])
    paises_agrupados.sort(key=lambda x: x[2], reverse=True)
    return paises_agrupados
        
