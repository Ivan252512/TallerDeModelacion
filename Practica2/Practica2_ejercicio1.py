""" Aproximar la primer derivada de f(x)=sin(x)+cos(pi*x-2*x**2)+x**3 en x=3*pi.
Usar fórmulas de diferencias finitias haci adelante, hacia atrás y centradas con
h=0.001;
Calcular la derivada analítica para medir el error relativo Err en cada caso."""
import numpy as np
x_i=3*np.pi
h=0.001

def fprimadex(x,h_0):
    f=np.sin(x+h_0)+np.cos(np.pi*(x+h_0)-2*(x+h_0)**2)+(x+h_0)**3
    return f

primerDerivada=(fprimadex(3*np.pi,h)-fprimadex(3*np.pi,0))/h
print(primerDerivada)


"""Derivada analítica f'(x)=cos(x)-sen(pi*x-2*x**2)*(pi-4x)+3*x**2"""

x=x_i
"""Derivada analítica"""
derAnalitica=np.cos(x)-np.sin(np.pi*x-2*x**2)*(np.pi-4*x)+3*x**2
print(derAnalitica)


"""Error relativo"""

err=np.absolute((derAnalitica-primerDerivada)/derAnalitica)*100
print(err)
