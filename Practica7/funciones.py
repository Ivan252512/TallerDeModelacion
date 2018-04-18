import numpy as np
import sympy
import matplotlib.pyplot as plt

def rk4_1d(f,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    x[0], y[0] = VI
    for i in range(1,N+1):
        k1 = f(x[i-1], y[i-1])
        k2 = f((x[i-1] + ((1/2)*h)), (y[i-1] + (1/2)*k1*h))
        k3 = f(x[i-1] + ((1/2)*h), (y[i-1] + (1/2)*k2*h))
        k4 = f((x[i-1] + h), (y[i-1] + k3*h))
        y[i] = y[i-1] + ((1/6)*(k1 + 2*k2 + 2*k3 + k4)*h)
    #Verificamos que los arreglos tengan la misma longitud, ya que el dominio y
    #el tamaño de nuestra h, provocan que un arreglo sea más grande.
    if(len(x)>len(y)):
        x=x[:len(x)-(len(x)-len(y))]
    if(len(y)>len(x)):
        y=y[:len(y)-(len(y)-len(x))]
    return x,y
