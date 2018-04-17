'''
c)Atractor de Lorenz:
x'=\sigma (y-x) \qquad \sigma=0.7
y'=\rho x-y-xy \qquad \rho=0.5
z'=-\beta z+xy \qquad \beta=0.5
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import funciones

n = -100.0
m = 100.0
# Tamaño
h = 0.01
# Valor Inicial: y(0.0) = 1.0
VI = (8.0,1.0,1.0) #(x,y,y')

sigma=10
rho=28
beta=8/3

def f(x,y,z):
    global sigma,rho,beta
    return sigma*(y-x)

def g(x,y,z):
    global sigma,rho,beta
    return x*(rho-z)-y

def e(x,y,z):
    global sigma,rho,beta
    return -beta*z+x*y

#rk4(funcion,x[inicia],x[final],paso,valores iniciales,orden de la ED)
num=funciones.rk43ind(f,g,e,n,m,h,VI)


ax = plt.axes(projection='3d')
ax.plot3D(num[0], num[1], num[2])
plt.legend(loc=1)
plt.title("Atractor de Lorenz")
plt.ylabel('y')
plt.xlabel('x')
ax.set_zlabel('y´')
plt.show()
