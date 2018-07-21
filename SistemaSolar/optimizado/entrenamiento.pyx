"""El objetivo de este programa es crear una simulación de las fuerzas gravi-
tacionales que influyen en la trayectoria de una nave espacial en el sistema
solar y que parte desde la Tierra hacia otro planeta, también se utilizaron
algoritmos genéticos para encontrar las rutas que llevaras a la nave más cerca
de su destino."""

#Función de evaluación
#ag es el script donde están las funciones correspondientes a algoritmos
#genéticos.
import ag

"""Llamamos a la función evolución de ag y guardamos la última generación que
regresa"""
#f=función de evaluación
#-7.5,7.5 limites para vx y vy
#2500 limite para el tiempo de inicio de la nave, debe ser menor a 10000.
#ag.poblacion(100,20) genera una población de 100 cadenas binarias con 20 bits.
#25 son las generaciones.

optimo=ag.evolucion(-7.5, 7.5, 50000, ag.poblacion(50,15),
                    ag.poblacion(50,15), ag.poblacion(50,15), 30)
print(optimo)
#Guardamos en un .txt
optimos=open('optimos.txt', 'w')
for i in optimo:
    optimos.write(str(i)+'\n' )
optimos.close()
