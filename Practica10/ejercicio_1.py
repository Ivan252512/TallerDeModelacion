################################################################
############ Metodos de diferencias finitas ####################
############ Con condiciones de frontera tipo Dirichlet ########
################################################################
################################################################

import numpy as np
import matplotlib.pyplot as plt

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
            A[i,j-1]=-1
            A[i,j]=2+h**2
            A[i,j+1]=-1

A[0,0]=2+h**2
A[0,1]=-1
A[N-1,N-2]=-1
A[N-1,N-1]=2+h**2

#Crear vector de soluciones
f=np.zeros((N,1))
for i in range(0,N):
    f[i]=1

#La matriz solucion!
u=np.matmul(A,f)
print(u)
