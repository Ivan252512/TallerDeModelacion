import matplotlib.pyplot as plt
import numpy as np
import funciones

"""Constantes en el sistema de ecuaciones diferenciales"""
L=50
T=300
W=50
E=12000000
I=4

"""Funciones a resolver"""
def f(x,y,u1,y2,u2):
    return x

def g(x,y,u1,y2,u2):
    return u1

def e(x,y,u1,y2,u2):
    return (T/(E*I))*y+(W*x*(x-L))/(2*E*I)

def k(x,y,u1,y2,u2):
    return u2

def l(x,y,u1,y2,u2):
    return T/(E*I)*y2

a=0; #Inicio del dominio.
b=L; #Fin del dominio.
stp=0.1; #Pasos entre cada punto.

num=funciones.rk45ind(f,g,e,k,l,a,b,stp,[0,0,0,1])

#y(t)=y1(t)+beta-(y1(b)/y2(b))*y2(t)  ,y2(b)!=0
beta=0

ydet=(np.array(num[1])+beta-((num[1][len(num[1])-1])/num[3][len(num[3])-1]) *
     np.array(num[3]))

plt.figure(figsize=(40,20))
plt.plot(num[0],ydet,label='y(t)=y1(t)+beta-(y1(b)/y2(b))*y2(t) ,beta=0 ')
plt.title("Práctica 8")
plt.ylabel("y(t)")
plt.xlabel('t')
plt.legend(loc=2)
plt.savefig( 'practica8.png', fmt='PNG', dpi=400 )
plt.show()
