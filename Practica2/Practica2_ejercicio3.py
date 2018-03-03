"""Aproximar la segunda parcial con respecto a x para
f(x,y,x)=(e**(x**2+sqrt(|x-y+5z|))*sin(x**2+1))/(x**2+2) con (sqrt(2),pi,0)"""

import numpy as np
x_i=np.sqrt(2)
y_i=np.pi
z_i=0
h_0=0.001

def Segundaparcialdefdex(x,y,z,h):
    f=((np.exp(x**2+np.sqrt(np.absolute(x-y+5*z))))/(x**2+2))*(np.sin(x**2+1))
    fmash=((np.exp((x+h)**2+np.sqrt(np.absolute((x+h)-y+5*z))))/((x+h)**2+2))*(np.sin((x+h)**2+1))
    fmenosh=((np.exp((x-h)**2+np.sqrt(np.absolute((x-h)-y+5*z))))/((x-h)**2+2))*(np.sin((x-h)**2+1))
    segundaparcialdex=(fmash-(2**f)+fmenosh)/(h**2)

    return segundaparcialdex

segundaDerivadaParcialdex=Segundaparcialdefdex(x_i,y_i,z_i,h_0)
print(segundaDerivadaParcialdex)
