"""Aproximar la segunda derivada de f(x)=2**(sin(x**2+1))*cos(sqrt(|sin(x-1)|))
en x=sqrt(2), usar h=0.001 y diferencias centradas"""

import numpy as np
x_i=np.sqrt(2)
h_0=0.001

def f2primadex(x,h):
    f=2**(np.sin(x**2+1))*np.cos(np.sqrt(np.absolute(np.sin(x-1))))
    fmash=2**(np.sin((x+h)**2+1))*np.cos(np.sqrt(np.absolute(np.sin((x+h)-1))))
    fmenosh=2**(np.sin((x-h)**2+1))*np.cos(np.sqrt(np.absolute(np.sin((x-h)-1))))
    f2prima=(fmenosh-2*f+fmash)/((h)**2)

    return f2prima

segundaDerivada=f2primadex(x_i,h_0)
print(segundaDerivada)
