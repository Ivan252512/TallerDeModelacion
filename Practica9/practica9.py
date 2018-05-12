#################################################################################
#	Ejercicio. Resolver numéricamente el PVI:				#
#		y'' = -2yy' + ty' + y + t 					#
#		y(1) = 0, y(2) = -2 en 1 <= t <= 2				#
#	Usar el método de Runge-Kutta con h=0.01 y una tolerancia de 10⁻⁷	#
#	Graficar los disparos en una misma figura.				#
#################################################################################
import funciones as rk
import matplotlib.pyplot as plt
import numpy as np

""" Solución """

def g(t, y, yp, z, zp ):
	return yp

def e(t, y, yp, z, zp ):
	return -2*(y*yp+t*yp+y+t)

def k(t, y, yp, z, zp ):
	return zp

def l(t, y, yp, z, zp ):
	return z*(-2*yp-2)+zp*(-2*y-2*t)

a=1; #Inicio del dominio.
b=2; #Fin del dominio.
stp=0.01; #Pasos entre cada punto.
m0=-2

while
num=rk.rk45ind(g,e,k,l,a,b,stp,[0,m0,0,1])
#y(t)=y1(t)+beta-(y1(b)/z(b))*z(t)  ,z(b)!=0

w=abs(num[1][len(num[1])-1]-(-2))
m0=m0-((num[1][len(num[1])-1]-(-2))/num[3][len(num[3])-1])


ydet=(np.array(num[1])+beta-((num[1][len(num[1])-1])/num[3][len(num[3])-1]) *
     np.array(num[3]))

plt.figure(figsize=(20,10))
plt.plot(num[0],ydet,label=" y'' = -2yy' + ty' + y + t ")
plt.title("Práctica 9 ")
plt.ylabel("y(t)")
plt.xlabel('t')
plt.legend(loc=2)
plt.savefig( 'practica9.png', fmt='PNG', dpi=400 )
plt.show()
