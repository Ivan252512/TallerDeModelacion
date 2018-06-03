

import numpy as np
import sympy
import matplotlib.pyplot as plt

def rk4(f,g,a,b,dt,VI):
    N=int((b-a)/dt)
    x = np.arange(a, b+dt, dt)
    y = np.zeros((N+1,))
    r = np.zeros((N+1,))
    x[0], y[0], r[0] = VI
    for i in range(1,N+1):
        k1x=dt*f(x[i-1],y[i-1],r[i-1])
        k1y=dt*g(x[i-1],y[i-1],r[i-1])
        k2x=dt*f(x[i-1]+dt/2,y[i-1]+k1x/2.0,r[i-1]+k1y/2.0)
        k2y=dt*g(x[i-1]+dt/2,y[i-1]+k1x/2.0,r[i-1]+k1y/2.0)
        k3x=dt*f(x[i-1]+dt/2,y[i-1]+k2x/2.0,r[i-1]+k2y/2.0)
        k3y=dt*g(x[i-1]+dt/2,y[i-1]+k2x/2.0,r[i-1]+k2y/2.0)
        k4x=dt*f(x[i-1]+dt,y[i-1]+k3x,r[i-1]+k3y)
        k4y=dt*g(x[i-1]+dt,y[i-1]+k3x,r[i-1]+k3y)
        y[i]=y[i-1]+(k1x+2.0*k2x+2.0*k3x+k4x)/6.0
        r[i]=r[i-1]+(k1y+2.0*k2y+2.0*k3y+k4y)/6.0
    return x,y,r

def rk43ind(f,g,e,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    z = np.zeros((N+1,))
    x[0], y[0], z[0] = VI
    for i in range(1,N+1):
        k1x = h*f(x[i-1], y[i-1], z[i-1])
        k1y = h*g(x[i-1], y[i-1], z[i-1])
        k1z = h*e(x[i-1], y[i-1], z[i-1])

        k2x = h*f(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0, z[i-1] + k1z/2.0)
        k2y = h*g(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0, z[i-1] + k1z/2.0)
        k2z = h*e(x[i-1]+ k1x/2.0, y[i-1] + k1y/2.0, z[i-1] + k1z/2.0)

        k3x = h*f(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0, z[i-1] + k2z/2.0)
        k3y = h*g(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0, z[i-1] + k2z/2.0)
        k3z = h*e(x[i-1]+ k2x/2.0, y[i-1] + k2y/2.0, z[i-1] + k2z/2.0)

        k4x = h*f(x[i-1]+ k3x, y[i-1] + k3y, z[i-1] + k3z)
        k4y = h*g(x[i-1]+ k3x, y[i-1] + k3y, z[i-1] + k3z)
        k4z = h*e(x[i-1]+ k3x, y[i-1] + k3y, z[i-1] + k3z)

        x[i] = x[i-1] + k1x/6.0 + k2x/3.0 + k3x/3.0 + k4x/6.0
        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
        z[i] = z[i-1] + k1z/6.0 + k2z/3.0 + k3z/3.0 + k4z/6.0
    return x,y,z
