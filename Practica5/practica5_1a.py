"""Usando R-K de 2do orden (Heun) al problema de valor inicial
y'=-2x**3+12x**2-20x+8.5 con h=0.5"""
import matplotlib.pyplot as plt
import funciones

# límites: 0.0 <= x <= 4.0
n = 0.0
m = 4.0
# Tamaño
h = 0.5
# Valor Inicial: y(0.0) = 1.0
VI = (0.0,1.0)

# EDO
def f(x,y):
    return -2*(x**3)+12*(x**2)-20*x+8.5

# Solución analítica
def y(x):
    return -(1/2)*(x**4)+4*(x**3)-10*(x**2)+8.5*x+1


num=funciones.heun_method(f,n,m,h,VI)
analitica=funciones.evalua(y,n,m,h,VI)
error=funciones.errorRelativoArray(analitica[1],num[1])

plt.subplot(211)
plt.plot(num[0],num[1],label='Numérica')
plt.plot(analitica[0],analitica[1],label='Analítica')
plt.legend(loc=2)
plt.title("Método de Heun")
plt.ylabel('y(x)')
plt.subplot(212)
plt.plot(num[0],error,label='Error')
plt.legend(loc=2)
plt.xlabel('x(h=0.5)')
plt.ylabel('Error [%]')
plt.savefig( 'Heun.png', fmt='PNG', dpi=100 )
plt.show()
