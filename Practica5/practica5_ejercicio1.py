import math
import numpy as np
import matplotlib.pyplot as plt

def heun( f, a, b, N, IV ):
    h = (b-a)/float(N)
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        f1 = f( t[i-1], w[i-1] )
        f2 = f( t[i-1] + (2.0/3.0) * h, w[i-1] + (2.0/3.0) * h * f1 )
        w[i] = w[i-1] + h * ( f1 + 3.0 * f2 ) / 4.0
    return w,t


def euler( f, a, b, N, IV ):
    h = (b-a)/float(N)
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        w[i] = w[i-1] + h * f( t[i-1], w[i-1] )
    return w,t

def evalua(f,a,b,N,IV):
    h=(b-a)/float(N)
    t=np.arange(a,b+h,h)
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        w[i] = f(t[i-1],w[i-1])
    return w,t


def errorRelativoArray(analitica,numerica):
    if (len(analitica)==len(numerica)):
        error=[]
        for i in range(len(analitica)):
            error.append(np.absolute((analitica[i]-numerica[i])/analitica[i])*100)
        return error;


def f(x,y):
    return 2*x*y

#Analitic e**(x**2-1)
def f1(x,y):
    return np.exp(x**2-1)

heun=np.array(heun(f,1,5,10,[1,1]))
euler=np.array(euler(f,1,5,10,[1,1]))
analitica=np.array(evalua(f1,1,5,10,[1,1]))

heunError=np.array(errorRelativoArray(analitica[0],heun[0]))
eulerError=np.array(errorRelativoArray(analitica[0],euler[0]))


def sumaDeArreglos(array1,array2):
    if (len(array1)==len(array2)):
        res=[]
        for i in range(len(array1)):
            res.append(array1[i]+array2[i])
        return error;
print(heun)
print(heunError)
print(eulerError)

plt.plot( heun[1], heun[0], label='Heun' )
plt.plot( euler[1], euler[0], label='Euler' )
plt.plot(analitica[1],analitica[0],label='Analítica')
plt.title( "Comparación" )
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(loc=1)
plt.grid()
plt.savefig( 'ecomparacion.png', fmt='PNG', dpi=100 )
plt.show()
