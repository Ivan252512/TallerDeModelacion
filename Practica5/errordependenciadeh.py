import funciones
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return -2*(x**3)+12*(x**2)-20*x+8.5

def y(x):
    return -(1/2)*(x**4)+4*(x**3)-10*(x**2)+8.5*x+1

# límites: 0.0 <= x <= 4.0
n = 0.0
m = 5.0
# Tamaño
# Valor Inicial: y(0.0) = 1.0
VI = (0.0,1.0)

errorArray=[]
errorArray1=[]
hArray=[]

for h in range(1,10):
    num=funciones.heun_method(f,n,m,h/100,VI)
    analitica=funciones.evalua(y,n,m,h/100,VI)
    error=funciones.errorRelativoArray(analitica[1],num[1])
    print(error)
    errorArray.append(error[2])
    errorArray1.append(error[1])
    hArray.append(h/100)



plt.plot(hArray,errorArray,label='2')
plt.plot(hArray,errorArray1,label='1')
plt.legend()
plt.xlabel("h")
plt.ylabel("Error")
plt.show()
