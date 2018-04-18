import matplotlib.pyplot as plt
import funciones

def f(t,y):
    return y**2
a=0;
b=0.4999;
y0=2;
stp=0.01;

num=funciones.rk4_1d(f,a,b,stp,[0,2])


plt.plot(num[0],num[1],label='f(t,y)=y²')
plt.title("Práctica 7")
plt.ylabel("y(t)")
plt.xlabel('t')
plt.legend(loc=2)
plt.savefig( 'practica7.png', fmt='PNG', dpi=100 )
plt.show()
