""""Usando R-K de 2do orden (Punto Medio) al problema de valor inicial
y'=-2x**3+12x**2-20x+8.5 con h=0.5"""
import matplotlib.pyplot as plt
import funciones

# límites: 0 <= x <= 4
a = 0
b = 4
# tamaño
h = 0.5
# valor Inicial: y(0) = 1
VI = (0,1)

# EDO
def f(x,y):
    return -2*(x**3)+12*(x**2)-20*x+8.5

# Solución analítica
def y(x):
    return -(1/2)*(x**4)+4*(x**3)-10*(x**2)+8.5*x+1


num=funciones.puntomediometh(f, a, b, h, VI)
analitica=funciones.evalua(y,a,b,h,VI)
error=funciones.errorRelativoArray(analitica[1],num[1])

plt.subplot(211)
plt.plot(num[0],num[1],label='Numérica')
plt.plot(analitica[0],analitica[1],label='Analítica')
plt.legend(loc=2)
plt.title("Método Punto Medio")
plt.ylabel('y(x)')
plt.subplot(212)
plt.plot(num[0],error,label='Error')
plt.legend(loc=2)
plt.xlabel('x(h=0.5)')
plt.ylabel('Error [%]')
plt.savefig( 'PuntoMedio.png', fmt='PNG', dpi=100 )
plt.show()
