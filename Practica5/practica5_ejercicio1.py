import math
import numpy as np
import matplotlib.pyplot as plt

def heun_method( f, a, b, N, IV ):
    h = (b-a)/float(N)
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        f1 = f( t[i-1], w[i-1] )
        f2 = f( t[i-1] + (2.0/3.0) * h, w[i-1] + (2.0/3.0) * h * f1 )
        w[i] = w[i-1] + h * ( f1 + 3.0 * f2 ) / 4.0
    return w,t


def euler_mthd( f, a, b, N, IV ):
    h = (b-a)/float(N)
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        w[i] = w[i-1] + h * f( t[i-1], w[i-1] )
    return w,t


def errorRelativo(derAnalitica,derivadaNumerica):
    return np.absolute((derAnalitica-derivadaNumerica)/derAnalitica)*100


def f(x,y):
    return 2*x*y



heun=heun_method(f,1,5,10,[0,1])
euler=euler_mthd(f,1,5,10,[0,1])

#Analitic e**(x**2-1)


plt.plot( heun[1], heun[0], label='Heun' )
plt.plot( euler[1], euler[0], label='Euler' )
plt.title( "COmparación" )
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend(loc=4)
plt.grid()
plt.savefig( 'ecomparacion.png', fmt='PNG', dpi=100 )
plt.show()
