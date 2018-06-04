""" Programa para graficar las soluciones a las ecuaciones diferenciales"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Dos variables
def graf2Var(x, y, nombre, funcion, var0):
    plt.plot(x, y, label = funcion )
    plt.title(nombre)
    plt.xlabel(var0)
    plt.ylabel("F(" + str(var0) + ")")
    plt.legend(loc=1)
    plt.savefig( nombre +'_'+ funcion + '.png', fmt='PNG', dpi=100 )
    plt.show()

def graf3Var(x, y, z, nombre, funcion, var0, var1, var2):
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z,label=funcion)
    plt.legend(loc=1)
    plt.title(nombre)
    plt.ylabel(var1)
    plt.xlabel(var0)
    ax.set_zlabel(var2)
    plt.show()
