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
w=1e-6
beta=-2

plt.figure(figsize=(20,9))

while(w>1e-7):
	num=rk.rk45ind(g,e,k,l,a,b,stp,[0,m0,0,1])
	#y(t)=y1(t)+beta-(y1(b)/z(b))*z(t)  ,z(b)!=0
	ydet=(np.array(num[1])+((beta-((num[1][len(num[1])-1])))/
		  num[3][len(num[3])-1]) * np.array(num[3]))
	plt.subplot(211)
	plt.plot(num[0],ydet, label="w = " + str(w) + ", m0 = " + str(m0))
	plt.legend(loc=1)
	plt.title("Práctica 9 " +"\n" + "y'' = -2yy' + ty' + y + t")
	plt.ylabel("y(t)")

	plt.subplot(212)
	plt.plot(num[0],num[1])

	zb=num[3][len(num[3])-1]
	yb=num[1][len(num[1])-1]
	dif=yb-beta
	w=abs(dif)
	m0=m0-(dif/zb)
plt.plot(num[0],num[1],  linestyle='--', color='r',
		 label = "Mejor Solución")
plt.legend(loc=1)
plt.ylabel('y1(t)')
plt.xlabel('t')
plt.savefig( 'practica9.png', fmt='PNG', dpi=400 )
plt.show()
