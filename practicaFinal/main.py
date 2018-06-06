"""Trabajo fonal de taller de modelación, kit de herramientas"""

#Para convertir strings funciones.
from math import *
#Librería de matemáticas.
import numpy as np
#Mérodos numéricos.
import funciones
#Para graficar las soluciones.
import grafica
import matplotlib.pyplot as plt


# Número de funciones a utilizar
while True:
    try:
        numFunc = int(input('¿Cuántas funciones vas a utilizar?  '))
        if 0<numFunc<5:
            break
        print ('El valor debe estar entre 1 y 4, intenta de nuevo.')
    except ValueError:
        print ('Carácter no válido, debe ser un número entero.')

print('¿Alguna variable es independiente de todas las demás? 0 no y 1 sí')
print('Si no está seguro ingrese 1, p. ej. es cuando el tiempo es independiente')
dep = int(input('Ingrese 1 o 0: '))

#Asignación de variables
print('Introduce las variables que vas a utilizar (e.g x ó t ó z),'
      +' toma en cuenta que el número de variables es el número de'
      +' funciones más 1 (si alguna variable no depende de las demás).')
print('La variable de más es f(variable independiente), si te sobran variables'
      + ' pon culquier letra, p. ej y, es necesario para realizar el método.')
if numFunc==1:
    var0=input('Introduce tu variable 1:  ')
    var1=input('Introduce tu variable 2:  ')
if numFunc==2:
    var0=input('Introduce tu variable 1:  ')
    var1=input('Introduce tu variable 2:  ')
    var2=input('Introduce tu variable 3:  ')
if numFunc==3:
    var0=input('Introduce tu variable 1:  ')
    var1=input('Introduce tu variable 2:  ')
    var2=input('Introduce tu variable 3:  ')
    if dep==1:
        var3=input('Introduce tu variable 4:  ')
if numFunc==4:
    var0=input('Introduce tu variable 1:  ')
    var1=input('Introduce tu variable 2:  ')
    var2=input('Introduce tu variable 3:  ')
    var3=input('Introduce tu variable 4:  ')
    var4=input('Introduce tu variable 5:  ')

#Asignación de funciones
print('Introduce tus funciones, las constantes deben tener un valor'
      +' numérico y no ser literales:  ')
if numFunc==1:
    fs = input('Introduce tu función 1:  ')
    exec('f = lambda ' + var0 + ', ' + var1 + ' : ' + fs)
if numFunc==2:
    fs = input('Introduce tu función 1:  ')
    exec('f = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ' : ' + fs)
    gs = input('Introduce tu función 2:  ')
    exec('g = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ' : ' + gs)
if numFunc==3:
    if dep==1:
        fs = input('Introduce tu función 1:  ')
        exec('f = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
             ' : ' + fs)
        gs = input('Introduce tu función 2:  ')
        exec('g = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
             ' : ' + gs)
        es = input('Introduce tu función 3:  ')
        exec('e = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
             ' : ' + es)
    if dep==0:
        fs = input('Introduce tu función 1:  ')
        exec('f = lambda ' + var0 + ', ' + var1 + ', ' + var2 +
             ' : ' + fs)
        gs = input('Introduce tu función 2:  ')
        exec('g = lambda ' + var0 + ', ' + var1 + ', ' + var2 +
             ' : ' + gs)
        es = input('Introduce tu función 3:  ')
        exec('e = lambda ' + var0 + ', ' + var1 + ', ' + var2 +
             ' : ' + es)
if numFunc==4:
    fs = input('Introduce tu función 1:  ')
    exec('f = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
         ', ' + var4 + ' : ' + fs)
    gs = input('Introduce tu función 2:  ')
    exec('g = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
         ', ' + var4 + ' : ' + gs)
    es = input('Introduce tu función 3:  ')
    exec('e = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
         ', ' + var4 + ' : ' + es)
    os = input('Introduce tu función 4:  ')
    exec('l = lambda ' + var0 + ', ' + var1 + ', ' + var2 + ', ' + var3 +
         ', ' + var4 + ' : ' + os)

#Intervalo e iteraciones
a = float(input('Introduce el inicio del intervalo a evaluar: '))
b = float(input('Introduce el final del intervalo a evaluar:  '))
# h
h = float(input('Introduce el desplazamiento entre cada iteración (h): '))
# Valores iniciales
VI=[a]
print('El valor inicial para tu variable 1 es a = ' + str(a) )
for i in range(numFunc):
    VI.append(float(input('Introduce el valor inicial para tu variable ' +
                          str(i+2) + ':  ')))
    if dep==0 and i==numFunc-2:
        break

#Escoger el método para resolver
if numFunc==1:
    print('Médotos numéricos, introduce el número correspondiente:  ')
    print('0 : Heun')
    print('1 : Euler')
    print('2 : Punto medio')
    print('3 : Ralston')
    print('4 : Runge-Kutta 4° orden')
    print('5 : Runge-Kutta 5° orden')
    chose = input('Escoge el método para resolver tu ecuación:  ')
    if chose=='0':
        x, y = funciones.heun(f, a, b, h, VI)
        grafica.graf2Var(x, y, 'Heun', fs, var0)
    if chose=='1':
        x, y  = funciones.euler(f, a, b, h, VI)
        grafica.graf2Var(x, y, 'Euler', fs, var0)
    if chose=='2':
        x, y  = funciones.puntomediometh(f, a, b, h, VI)
        grafica.graf2Var(x, y, 'Punto medio', fs, var0)
    if chose=='3':
        x, y  = funciones.Ralston_meth(f, a, b, h, VI)
        grafica.graf2Var(x, y, 'Ralston', fs, var0)
    if chose=='4':
        x, y  = funciones.rk41D(f, a, b, h, VI)
        grafica.graf2Var(x, y, 'Runge-Kutta 4° orden', fs, var0)
    if chose=='5':
        x, y  = funciones.rk51D(f, a, b, h, VI)
        grafica.graf2Var(x, y, 'Runge-Kutta 5° orden', fs, var0)

if numFunc==2:
    print('El método que se utilizará es Runge-Kutta 4° orden')
    x, y, z = funciones.rk43d(f, g, a, b, h, VI)
    grafica.graf3Var(x, y, z, 'Runge-Kutta 4° orden', 'f: ' + fs + '\n' + 'g :'
                     + gs, var0, var1, var2)

if numFunc==3:
    print('El método que se utilizará es Runge-Kutta 4° orden')
    if dep==0:
        x, y, z = funciones.rk43ind(f, g, e, a, b, h, VI)
        grafica.graf3Var(x, y, z, 'Runge-Kutta 4° orden', 'f: ' + fs + '\n'
                         + 'g :' + gs + '\n' + 'e :' + es, var0, var1, var2)
    if dep==1:
        print('Como no se pueden graficar 4 variables, solo se regresan los' +
              'valores.')
        print(funciones.rk44d(f, g, e, a, b, h, VI))

if numFunc==4:
    print('El método que se utilizará es Runge-Kutta 4° orden')
    print('Si desea implementar el método del disparo introduzca 1')
    print('Si desea solo resolver las ecuaciones introduzca 0')
    disp = input('Elección:  ')
    if disp=='0':
        print('Como no se pueden graficar 5 variables, solo se regresan los' +
              'valores.')
        print(funciones.rk45d(f, g, e, l, a, b, h, VI))
    if disp=='1':
        EDPNL = input('Introduzca su ecuación no lineal:  ')
        beta = float(input('Introduzca el valor de beta:  '))
        w = float(input('Introduzca el valor inicial de w:  '))
        lim = float(input('Introduzca el valor más pequeño que w puede tomar:'))
        while(w>lim):
            t, y, yp, z, zp = funciones.rk45d(f, g, e, l, a, b, h, VI)
            #y(t)=y1(t)+beta-(y1(b)/z(b))*z(t)  ,z(b)!=0
            ydet=(np.array(y)+((beta-((y[len(y)-1])))/
            	  z[len(z)-1]) * np.array(z))
            plt.plot(t,ydet, label="w = " + str(w) + ", m = " + str(VI[2]))
            plt.legend(loc=1)
            plt.title("Método de disparo: " + EDPNL)
            plt.ylabel("F(" + str(var0) + ")")

            zb=z[len(z)-1]
            yb=y[len(y)-1]
            dif=yb-beta
            w=abs(dif)
            VI[2]=VI[2]-(dif/zb)
        plt.xlabel('t')
        plt.savefig("Método de disparo: " + EDPNL + '.png', fmt='PNG', dpi=400 )
        plt.show()
