import numpy as np
import math
import random

"""Algoritmo genético"""

"""Genera cadenas binarias de n bits"""

def generaIndividuo(bits):
    cadena=""
    for i in range(bits):
        cadena+=str(random.randint(0, 1))
    return cadena

"""Convierte valores binarios a decimales con punto decimal, en el intervalo
   [a,b]"""

def binToDec(bin,a,b):
    n=len(bin)
    dec=0
    for i in bin:
        if i=='1':
            dec+=2**(n-1)
        n-=1
    return  a+((dec)/(2**len(bin)-1))*(b-a)

"""Algoritmo de reproducción, cruza los "genes" de dos individuos, se utiliza
   cruce uniforme"""

def cruza(bin1,bin2):
    if(len(bin1)==len(bin2)):
        hijo=""
        for i in range(len(bin1)):
            rand=random.randint(0,1)
            if (rand==0):
                hijo+=bin1[i]
            else:
                hijo+=bin2[i]
        return hijo
    else:
        return ("Los binarios deben tener la misma longitud difieren en " +
                 str(abs(len(bin1)-len(bin2))) + " dígitos.")

"""Algoritmo de mutación, cambia aleatoriamente el valor de un gen"""

def mutacion(bin):
    rand=random.randint(0,len(bin)-1)
    if(bin[rand]==0):
        bin[rand]="1"
    if(bin[rand]==1):
        bin[rand]="0"
    return bin

"""Crea una población de individuos"""
def poblacion(cantidad,bitsDeCadaIndividuo):
    pob=[]
    for i in range(cantidad):
        pob.append(generaIndividuo(bitsDeCadaIndividuo))
    return pob


"""Algoritmo de selección de mínimos, recibe una función de evaluación y una
   lista con individuos(cadenas de binarios) a evaluar, selecciona al 50% más
   apto, los reproduce y la descendencia remplaza al 50% menos apto"""


def evolucion(f,a,b,t,individuosx,individuosy,individuost,iteraciones):
    print("---------------------------------------------------------")
    if len(individuosx)!=len(individuosy)!=len(individuost):
        return "Las poblaciones iniciales deben tener la misma longitud."
    #Selección
    evaluacion=[]
    for i in range(len(individuosx)):
        evaluacion.append([f(binToDec(individuosx[i],a,b),
                             binToDec(individuosy[i],a,b),
                             int(binToDec(individuost[i],0,t))),
                             individuosx[i],
                             individuosy[i],
                             individuost[i]])
    evaluacion.sort()
    mejores50=evaluacion[:int(0.5*len(evaluacion))]
    #Reproducción
    hijos=[]
    mejores50bin=[]
    for i in range(len(mejores50)):
        mejores50bin.append([mejores50[i][1],mejores50[i][2],mejores50[i][3]])
        hijos.append([cruza(mejores50[random.randint(0,len(mejores50)-1)][1],
                            mejores50[random.randint(0,len(mejores50)-1)][1]),
                      cruza(mejores50[random.randint(0,len(mejores50)-1)][2],
                            mejores50[random.randint(0,len(mejores50)-1)][2]),
                      cruza(mejores50[random.randint(0,len(mejores50)-1)][3],
                            mejores50[random.randint(0,len(mejores50)-1)][3])])
    #Mutación, solo los hijos mutan, escogemos el 10% al azar, 2 veces.
    for i in range(int(len(hijos)*0.1)):
        for i in range(5):
            randx=random.randint(0,len(hijos)-1)
            hijos[randx][0]=mutacion(hijos[randx][0])
            randy=random.randint(0,len(hijos)-1)
            hijos[randy][1]=mutacion(hijos[randy][1])
            randt=random.randint(0,len(hijos)-1)
            hijos[randt][2]=mutacion(hijos[randt][2])
    #Junta a los padres y a los hijos
    nuevaGeneracion=mejores50bin+hijos
    genx=[]
    geny=[]
    gent=[]
    for i in range(len(nuevaGeneracion)):
        genx.append(nuevaGeneracion[i][0])
        geny.append(nuevaGeneracion[i][1])
        gent.append(nuevaGeneracion[i][2])
    if(iteraciones==0):
        decimales=[]
        for i in nuevaGeneracion:
            decimales.append([binToDec(i[0],a,b),binToDec(i[1],a,b),
                              int(binToDec(i[2],0,t))])
        return decimales
    else:
        return  evolucion(f,a,b,t,genx,geny,gent,iteraciones-1)
