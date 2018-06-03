################################################################
############ Metodos de diferencias finitas ####################
############ Con condiciones de frontera tipo Robin     ########
################################################################
################################################################

import numpy as np
import math

#Definir los vectores y el valor de las particiones
h=0.01
a=0
b=1
x=np.arange(a,b,h)
N=len(x)-2

A=np.zeros((N,N))
for i in range(1,N-2):
    for j in range(1,N-2):
        if i==j:
            A[i,j-1]=1
            A[i,j]=-2
            A[i,j+1]=1

A[0,0]=-2
A[0,1]=1
A[N-1,N-2]=1
A[N-1,N-1]=-2

#Crear vector de f

f=np.zeros((N,1))
f[0]=-math.cos(math.pi*x[i])*math.pi**2-1
for i in range(1,N-2):
    f[i]=-math.cos(math.pi*x[i])*math.pi**2
f[N-1]=-math.cos(math.pi*x[i])*math.pi**2+h*math.pi


f=f/(h**2);


#La matriz soluci�n!
u= np.matmul(A,f)

print(u)
