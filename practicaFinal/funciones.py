import numpy as np

"""Implementa el método de Runge-Kutta en 4 dimensiones"""
def rk45ind(g,e,k,l,a,b,h,VI):
    N=int((b-a)/h)
    t = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    yp = np.zeros((N+1,))
    z = np.zeros((N+1,))
    zp = np.zeros((N+1,))
    y[0], yp[0], z[0], zp[0] = VI
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

def rkRec():
    N=int((b-a)/h)
    t = np.arange(a, b+h, h)
    y = np.zeros(N+1,)
    y[0], yp[0], z[0], zp[0] = VI
    for i in range(1,N+1):
        k1y = h*g(t[i-1], y[i-1], yp[i-1], z[i-1], zp[i-1])
        k2y = h*g(t[i-1], y[i-1] + k1y/2.0, yp[i-1] + k1z/2.0,
                  z[i-1] + k1u/2.0, zp[i-1] + k1v/2.0)
        k3y = h*g(t[i-1], y[i-1] + k2y/2.0, yp[i-1] + k2z/2.0,
                  z[i-1] + k2u/2.0, zp[i-1] + k2v/2.0)
        k4y = h*g(t[i-1], y[i-1] + k3y, yp[i-1] + k3z, z[i-1] + k3u,
                  zp[i-1] + k3v)
        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
