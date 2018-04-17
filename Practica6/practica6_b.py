"""
b)Atractor de Rösler:
x'=-y-z
y'=x+Ay
z'=B+z(x-c)

Donde:
A=0.2 \qquad A=0.1
B=0.2 \qquad B=0.1
C=5.7 \qquad C<14
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import funciones

n = 0.0
m = 1000.0
# Tamaño
h = 0.01
# Valor Inicial: y(0.0) = 1.0
VI = (-9,0,0) #(x,y,y')

A=0.2
B=0.2
C=5.7

def f(x,y,z):
    global A,B,C
    return -y-z

def g(x,y,z):
    global A,B,C
    return x+A*y

def e(x,y,z):
    global A,B,C
    return B+z*(x-C)

#rk4(funcion,x[inicia],x[final],paso,valores iniciales,orden de la ED)
num=funciones.rk43ind(f,g,e,n,m,h,VI)


ax = plt.axes(projection='3d')
ax.plot3D(num[0], num[1], num[2],label='A=0.2,B=0.2,C=5.7')
plt.legend(loc=1)
plt.title("Atractor de Rösler 1 ")
plt.ylabel('y')
plt.xlabel('x')
ax.set_zlabel('y´')
plt.show()

A=0.1
B=0.1
C=14

num=funciones.rk43ind(f,g,e,n,m,h,VI)


ax = plt.axes(projection='3d')
ax.plot3D(num[0], num[1], num[2],label='A=0.1,B=0.1,C=14')
plt.legend(loc=1)
plt.title("Atractor de Rösler 2 ")
plt.ylabel('y')
plt.xlabel('x')
ax.set_zlabel('y´')
plt.show()
