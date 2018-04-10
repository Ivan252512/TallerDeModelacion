import numpy as np

def heun_method(f, n, m, h, VI):
    N=int((m-n)/h)
    x = np.arange(n, m+h, h)          # crear malla
    y = np.zeros((N+1,))                # ininio y
    x[0], y[0] = VI                     # valores iniciales
    for i in range(1,N+1):              # Aplicando método de Heun
        k1 = f(x[i-1], y[i-1])
        k2 = f(x[i-1]+h, y[i-1] + k1*h)
        y[i] = y[i-1] + ((1/2)*k1 + (1/2)*k2)*h
    return x,y

def puntomediometh(f, a, b, h, VI):
    N=int((b-a)/h)
    x = np.arange( a, b+h, h )
    y = np.zeros((N+1,))
    x[0], y[0] = VI
    for i in range(1,N+1):
        k1 = f(x[i-1],y[i-1])
        k2 = f(x[i-1] + (1/2)*h, y[i-1] + (1/2)*k1*h)
        y[i] = y[i-1] + (k2*h)
    return x,y

def Ralston_meth(f, n, m, h, VI):
    N=int((m-n)/h)
    x = np.arange(n, m+h, h)          # crear malla
    y = np.zeros((N+1,))                # inicio y
    x[0], y[0] = VI                     # valores iniciales
    for i in range(1,N+1):              # Aplicando método de Heun
        k1 = f(x[i-1], y[i-1])
        k2 = f(x[i-1]+(3/4)*h, y[i-1] + (3/4)*k1*h)
        y[i] = y[i-1] + ((1/3)*k1 + (2/3)*k2)*h
    return x,y

def rk4(f,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)          # malla
    y = np.zeros((N+1,))                # y
    x[0], y[0] = VI                     # valores iniciales
    for i in range(1,N+1):              # aplicando el método
        k1 = f(x[i-1], y[i-1])
        k2 = f((x[i-1] + ((1/2)*h)), (y[i-1] + (1/2)*k1*h))
        k3 = f(x[i-1] + ((1/2)*h), (y[i-1] + (1/2)*k2*h))
        k4 = f((x[i-1] + h), (y[i-1] + k3*h))
        y[i] = y[i-1] + ((1/6)*(k1 + 2*k2 + 2*k3 + k4)*h)
    return x,y

def rk5(f,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)          # malla
    y = np.zeros((N+1,))                # y
    x[0], y[0] = VI                     # valores iniciales
    for i in range(1,N+1):              # Aplicando el método
        k1 = f(x[i-1], y[i-1])
        k2 = f(x[i-1] + ((1/4)*h), y[i-1] + ((1/4)*k1*h))
        k3 = f(x[i-1] + ((1/4)*h), y[i-1] + ((1/8)*k1*h) + ((1/8)*k2*h))
        k4 = f(x[i-1] + ((1/2)*h), y[i-1] - ((1/2)*k2*h) + (k3*h))
        k5 = f(x[i-1] + ((3/4)*h), y[i-1] + ((3/16)*k1*h) + ((9/46)*k4*h))
        k6 = f(x[i-1], y[i-1] - ((3/7)*k1*h) + ((2/7)*k2*h) + ((12/7)*k3*h)
               + ((12/7)*k4*h) + ((8/5)*k5*h))
        y[i] = y[i-1] + ((1/90)*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*h)
    return x,y

#Evalua una función matemática
def evalua(f,a,b,h,IV):
    N=int((b-a)/h)
    x=np.arange(a,b+h,h)
    y = np.zeros((N+1,))
    x[0], y[0] = IV
    for i in range(1,N+1):
        y[i] = f(x[i])
    return x,y

def errorRelativoArray(analitica,numerica):
    if (len(analitica)==len(numerica)):
        analitica=np.array(analitica)
        numerica=np.array(numerica)
        error=(np.abs((analitica-numerica))/analitica)*100
        return error
