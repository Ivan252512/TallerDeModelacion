import numpy as np

def rk45ind(f,g,e,k,l,a,b,h,VI):
    N=int((b-a)/h)
    x = np.arange(a, b+h, h)
    y = np.zeros((N+1,))
    z = np.zeros((N+1,))
    y2 = np.zeros((N+1,))
    z2 = np.zeros((N+1,))
    y[0], z[0], y2[0], z2[0] = VI
    for i in range(1,N+1):
        k1y = h*g(x[i-1], y[i-1], z[i-1], y2[i-1], z2[i-1])
        k1z = h*e(x[i-1], y[i-1], z[i-1], y2[i-1], z2[i-1])
        k1u = h*k(x[i-1], y[i-1], z[i-1], y2[i-1], z2[i-1])
        k1v = h*l(x[i-1], y[i-1], z[i-1], y2[i-1], z2[i-1])


        k2y = h*g(x[i-1], y[i-1] + k1y/2.0, z[i-1] + k1z/2.0,
                  y2[i-1] + k1u/2.0, z2[i-1] + k1v/2.0)
        k2z = h*e(x[i-1], y[i-1] + k1y/2.0, z[i-1] + k1z/2.0,
                  y2[i-1] + k1u/2.0, z2[i-1] + k1v/2.0)
        k2u = h*k(x[i-1], y[i-1] + k1y/2.0, z[i-1] + k1z/2.0,
                  y2[i-1] + k1u/2.0, z2[i-1] + k1v/2.0)
        k2v = h*l(x[i-1], y[i-1] + k1y/2.0, z[i-1] + k1z/2.0,
                  y2[i-1] + k1u/2.0, z2[i-1] + k1v/2.0)


        k3y = h*g(x[i-1], y[i-1] + k2y/2.0, z[i-1] + k2z/2.0,
                  y2[i-1] + k2u/2.0, z2[i-1] + k2v/2.0)
        k3z = h*e(x[i-1], y[i-1] + k2y/2.0, z[i-1] + k2z/2.0,
                  y2[i-1] + k2u/2.0, z2[i-1] + k2v/2.0)
        k3u = h*k(x[i-1], y[i-1] + k2y/2.0, z[i-1] + k2z/2.0,
                  y2[i-1] + k2u/2.0, z2[i-1] + k2v/2.0)
        k3v = h*l(x[i-1], y[i-1] + k2y/2.0, z[i-1] + k2z/2.0,
                  y2[i-1] + k2u/2.0, z2[i-1] + k2v/2.0)


        k4y = h*g(x[i-1], y[i-1] + k3y, z[i-1] + k3z, y2[i-1] + k3u,
                  z2[i-1] + k3v)
        k4z = h*e(x[i-1], y[i-1] + k3y, z[i-1] + k3z, y2[i-1] + k3u,
                  z2[i-1] + k3v)
        k4u = h*k(x[i-1], y[i-1] + k3y, z[i-1] + k3z, y2[i-1] + k3u,
                  z2[i-1] + k3v)
        k4v = h*l(x[i-1], y[i-1] + k3y, z[i-1] + k3z, y2[i-1] + k3u,
                  z2[i-1] + k3v)

        y[i] = y[i-1] + k1y/6.0 + k2y/3.0 + k3y/3.0 + k4y/6.0
        z[i] = z[i-1] + k1z/6.0 + k2z/3.0 + k3z/3.0 + k4z/6.0
        y2[i] = y2[i-1] + k1u/6.0 + k2u/3.0 + k3u/3.0 + k4u/6.0
        z2[i] = z2[i-1] + k1v/6.0 + k2v/3.0 + k3v/3.0 + k4v/6.0
    return x,y,z,y2,z
