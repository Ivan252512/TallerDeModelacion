"""
Ejercicio: Implementar funciones para los métodos de Runge-Kutta de 4°orden en
2 y 3 dimensiones para resolver:

a) El PVI:
y''+xy'+y=0, y''(x,y,y')=-xy'-y
x=[0,10]
y(0)=1  & y'(0)=2
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import funciones

# límites: 0.0 <= x <= 4.0
n = 0.0
m = 10.0
# Tamaño
h = 0.01
# Valor Inicial: y(0.0) = 1.0
VI = (0.0,1.0,2.0) #(x,y,y')

# EDO r=yprim
def f(x,y,r):
    return -x*r-y

def g(x,y,r):
    return r

#rk4(funcion,x[inicia],x[final],paso,valores iniciales,orden de la ED)
num=funciones.rk4(f,g,n,m,h,VI)


ax = plt.axes(projection='3d')
ax.plot3D(num[0], num[1], num[2], label="y''=-xy'-y")
plt.legend(loc=1)
plt.title("Runge-Kutta 4° orden")
plt.ylabel('y')
plt.xlabel('x')
ax.set_zlabel('y´')
plt.show()
