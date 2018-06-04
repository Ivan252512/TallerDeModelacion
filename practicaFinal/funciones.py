import numpy as np

def heun( f, a, b, h, IV ):
    N=int((b-a)/h)
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        f1 = f( t[i-1], w[i-1] )
        f2 = f( t[i-1] + (2.0/3.0) * h, w[i-1] + (2.0/3.0) * h * f1 )
        w[i] = w[i-1] + h * ( f1 + 3.0 * f2 ) / 4.0
    return t,w


def euler( f, a, b, h, IV ):
    N=int((b-a)/h)
    t = np.arange( a, b+h, h )
    w = np.zeros((N+1,))
    t[0], w[0] = IV
    for i in range(1,N+1):
        w[i] = w[i-1] + h * f( t[i-1], w[i-1] )
    return t,w


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

def rk41D(f,a,b,h,VI):
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

def rk51D(f,a,b,h,VI):
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


def rk43d(g,e,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    z = np.zeros((N+1,))
    x[0], y[0], z[0] = VI
    for i in range(1,N+1):
        k1y = h*g(x[i-1], y[i-1], z[i-1])
        k1z = h*e(x[i-1], y[i-1], z[i-1])

        k2y = h*g(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0, z[i-1] + k1z/2.0)
        k2z = h*e(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0, z[i-1] + k1z/2.0)

        k3y = h*g(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0, z[i-1] + k2z/2.0)
        k3z = h*e(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0, z[i-1] + k2z/2.0)

        k4y = h*g(x[i-1]+ k3x, y[i-1] + k3y, z[i-1] + k3z)
        k4z = h*e(x[i-1]+ k3x, y[i-1] + k3y, z[i-1] + k3z)

        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
        z[i] = z[i-1] + k1z/6.0 + k2z/3.0 + k3z/3.0 + k4z/6.0
    return x,y,z

def rk44d(g,e,k,a,b,h,VI):
    N=int((b-a)/h)
    t = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    yp = np.zeros((N+1,))
    z = np.zeros((N+1,))
    t[0], y[0], yp[0], z[0] = VI
    for i in range(1,N+1):
        k1y = h*g(t[i-1], y[i-1], yp[i-1], z[i-1])
        k1z = h*e(t[i-1], y[i-1], yp[i-1], z[i-1])
        k1u = h*k(t[i-1], y[i-1], yp[i-1], z[i-1])


        k2y = h*g(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0)
        k2z = h*e(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0)
        k2u = h*k(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0)


        k3y = h*g(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0)
        k3z = h*e(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0)
        k3u = h*k(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0)


        k4y = h*g(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u)
        k4z = h*e(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u)
        k4u = h*k(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u)

        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
        yp[i] = yp[i-1] + k1z/6.0 + k2z/3.0 + k3z/3.0 + k4z/6.0
        z[i] = z[i-1] + k1u/6.0 + k2u/3.0 + k3u/3.0 + k4u/6.0
    return t,y,yp,z



def rk45d(g,e,k,l,a,b,h,VI):
    N=int((b-a)/h)
    t = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    yp = np.zeros((N+1,))
    z = np.zeros((N+1,))
    zp = np.zeros((N+1,))
    t[0], y[0], yp[0], z[0], zp[0] = VI
    for i in range(1,N+1):
        k1y = h*g(t[i-1], y[i-1], yp[i-1], z[i-1], zp[i-1])
        k1z = h*e(t[i-1], y[i-1], yp[i-1], z[i-1], zp[i-1])
        k1u = h*k(t[i-1], y[i-1], yp[i-1], z[i-1], zp[i-1])
        k1v = h*l(t[i-1], y[i-1], yp[i-1], z[i-1], zp[i-1])


        k2y = h*g(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0, zp[i-1] + k1v/2.0)
        k2z = h*e(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0, zp[i-1] + k1v/2.0)
        k2u = h*k(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0, zp[i-1] + k1v/2.0)
        k2v = h*l(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0, zp[i-1] + k1v/2.0)


        k3y = h*g(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0, zp[i-1] + k2v/2.0)
        k3z = h*e(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0, zp[i-1] + k2v/2.0)
        k3u = h*k(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0, zp[i-1] + k2v/2.0)
        k3v = h*l(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0, zp[i-1] + k2v/2.0)


        k4y = h*g(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u,
                  zp[i-1] + k3v)
        k4z = h*e(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u,
                  zp[i-1] + k3v)
        k4u = h*k(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u,
                  zp[i-1] + k3v)
        k4v = h*l(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u,
                  zp[i-1] + k3v)

        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
        yp[i] = yp[i-1] + k1z/6.0 + k2z/3.0 + k3z/3.0 + k4z/6.0
        z[i] = z[i-1] + k1u/6.0 + k2u/3.0 + k3u/3.0 + k4u/6.0
        zp[i] = zp[i-1] + k1v/6.0 + k2v/3.0 + k3v/3.0 + k4v/6.0
    return t,y,yp,z,zp
