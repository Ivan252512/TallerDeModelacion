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
#Unidad astronómica en KM para convertir km/hr en UA/año
UAkm = 1.496e+8 #km
vMaxCohete = (11000/UAkm)

optimo=ag.evolucion(-10, 10, 5000, ag.poblacion(10,15),
                    ag.poblacion(10,15), ag.poblacion(10,15), 5)
print(optimo)
#Guardamos en un .txt
optimos=open('noop/optimos.txt', 'w')
for i in optimo:
    optimos.write(str(i)+'\n' )
optimos.close()
