import cuerposCelestes as cc
import numpy as np


#Constantes
G= 39.4784176 # AU³ YR⁻² SM-¹
UAkm = 1.496e+8 #km
Msol = 1.989e+30 #kg
ANG= np.pi/2
sa = np.sin(ANG)
ca = np.cos(ANG)
sca = np.sin(np.pi/2+ANG)
cca = np.cos(np.pi/2+ANG)

#Diferencial a usar
dt= 60 * 3.17097889e-8 #1 min

"""Mercurio"""
rmerc=0.38          #radio
mmerc=0.166e-6      #masa
vmerc=np.sqrt(G/rmerc) #velocidad tangencial
wmerc=vmerc/rmerc   #velocidad angular

"""Venus"""
rvenus=0.723
mvenus=2.44e-6
vvenus=np.sqrt(G/rvenus)
wvenus=vvenus/rvenus

"""Tierra"""
rearth = 1
mearth = 3.004e-6
vearth = np.sqrt(G/rearth)
wearth = vearth/rearth

"""Luna"""
rluna = 1 + (356000/UAkm)
mluna = (7.349e+22)/Msol
vluna = np.sqrt(G/rluna) + (2412743/UAkm)/(27.32/365)
wluna = vluna/rluna

"""Marte"""
rmarte=1.53 #Distancia media al Sol del planeta de destino UA
mmarte=3.214e-7 #Masa del planeta de destino MS
vmarte=np.sqrt(G/rmarte)  #Velocidad de Marte
wmarte=vmarte/rmarte   # Velocidad angular de Marte

"""Satélites de Júpiter"""
"""Io"""
rio = 5.2 + (421600/UAkm)
mio = (8.94e+22)/Msol
vio = np.sqrt(G/rio) + (17.334/UAkm)*(60*60*24*365)
wio = vio/rio

"""Europa"""
reuropa = 5.2 + (671100/UAkm)
meuropa = (4.8e+22)/Msol
veuropa = np.sqrt(G/reuropa) + (13.740/UAkm)*(60*60*24*365)
weuropa = veuropa/reuropa

"""Ganimedes"""
rgan = 5.2 + (1070400/UAkm)
mgan = (1.48e+23)/Msol
vgan = np.sqrt(G/rgan) + (10.88/UAkm)*(60*60*24*365)
wgan = vgan/rgan

"""Calisto"""
rcal = 5.2 + (1882770/UAkm)
mcal = (1.08e+23)/Msol
vcal = np.sqrt(G/rcal) + (8.204/UAkm)*(60*60*24*365)
wcal = vcal/rcal

"""Jupiter"""
rjup=5.2
mjup=954.79e-6 #-4
vjup=np.sqrt(G/rjup)
wjup=vjup/rjup

"""Satélite más grande de Saturno"""
"""Titán"""
rtit = 9.57 + 1221870/UAkm
mtit = (1.345e+23)/Msol
vtit = np.sqrt(G/rtit) + (5.57/UAkm)*(60*60*24*365)
wtit = vtit/rtit

"""Saturno"""
rsat=9.57
msat=285.88e-6
vsat=np.sqrt(G/rsat)
wsat=vsat/rsat

"""Urano"""
rur=19.3
mur=43.66e-6
vur=np.sqrt(G/rur)
wur=vur/rur

"""Neptuno"""
rnep=30.2
mnep=51.51e-6
vnep=np.sqrt(G/rnep)
wnep=vnep/rnep

Sun = cc.celestialBody(1.0, 695508/UAkm, np.array([0.0,0.0,0.0]),
                       np.array([0.0,0.0,0.0]))

Mercury = cc.celestialBody(mmerc, 2440/UAkm, np.array([rmerc*ca, rmerc*sa,0]),
                           np.array([vmerc*cca, vmerc*sca, 0]))

Venus = cc.celestialBody(mvenus, 6052/UAkm, np.array([rvenus*ca,rvenus*sa,0]),
                        np.array([vvenus*cca, vvenus*sca, 0]))

Luna = cc.celestialBody(mluna, 1737/UAkm, np.array([rluna*ca,rluna*sa,0]),
                        np.array([vluna*cca, vluna*sca, 0]))

Earth = cc.celestialBody(mearth, 6371/UAkm, np.array([rearth*ca,rearth*sa,0.0]),
                         np.array([vearth*cca,vearth*sca,0.0]))

Mars = cc.celestialBody(mmarte, 3390/UAkm, np.array([rmarte*ca,rmarte*sa,0]),
                        np.array([vmarte*cca, vmarte*sca, 0]))

Io = cc.celestialBody(mio, 1822/UAkm, np.array([rio*ca,rio*sa,0]),
                        np.array([vio*cca, vio*sca, 0]))

Europa = cc.celestialBody(meuropa, 1561/UAkm, np.array([reuropa*ca,reuropa*sa,0]),
                        np.array([veuropa*cca, veuropa*sca, 0]))

Ganimedes = cc.celestialBody(mgan, 2634/UAkm, np.array([rgan*ca,rgan*sa,0]),
                        np.array([vgan*cca, vgan*sca, 0]))

Calisto = cc.celestialBody(mcal, 2410/UAkm, np.array([rcal*ca,rcal*sa,0]),
                        np.array([vcal*cca, vcal*sca, 0]))

Jupyter = cc.celestialBody(mjup, 0.1, np.array([rjup*ca,rjup*sa,0]),
                        np.array([vjup*cca, vjup*sca, 0]))

Titan = cc.celestialBody(mtit, 0.1, np.array([rtit*ca,rtit*sa,0]),
                        np.array([vtit*cca, vtit*sca, 0]))

Saturn = cc.celestialBody(msat, 0.1, np.array([rsat*ca,rsat*sa,0]),
                        np.array([vsat*cca, vsat*sca, 0]))

Uranus = cc.celestialBody(mur, 0.1, np.array([rur*ca,rur*sa,0]),
                            np.array([vur*cca, vur*sca, 0]))

Neptune = cc.celestialBody(mnep, 0.1, np.array([rnep*ca,rnep*sa,0]),
                        np.array([vnep*cca, vnep*sca, 0]))

movBody = [Sun,Mercury,Venus,Luna,Earth,Mars,Io,Europa,Ganimedes,
              Calisto,Jupyter,Titan,Saturn,Uranus,Neptune]

destino = Mars #Destino, se puede cambiar a cualquier planeta o Satélite.

"""Es la función principal, descripción en el archivo .pdf adjunto"""
def f(vx,vy,inicio):
    global movBody, dt, Msol, Earth, destino, UAkm, Luna

    tiempoLimite = 60*24*365 #Número máximo de iteraciones.
    tiempo = 0
    tiempoEnOrbita = 0

    #Condición de penalización para que la rapidez de la nave no supere el
    #límite impuesto.
    if not (40320/UAkm)*(24*365)<np.sqrt(vx**2+vy**2)<(60000/UAkm)*(24*365):
        #Imprime los valores a evaluar y su resultado.
        print(vx,vy,inicio,100)
        return 100

    posiciones=[]

    while True:
        #Tiempo inicial del viaje de la nave, es decir, la nave puede iniciar
        #su trayectoria mucho después de que se inicie la simulación.

        if tiempo==inicio:
            #cambiamos la posición inicial de la nave a la actual de la Tierra.
            Ship = cc.celestialBody(546700/Msol, 0.1/UAkm,
                   Earth.pos+np.array([0.0,Earth.radius,0.0]),
                   Earth.vel+np.array([vx, vy, 0.0]))
            movBody.append(Ship)
            #Primer distancia Nave-destino, se usa abajo, se le resta un poco a
            #conveniencia, para lograr que las trayectorias se encaminen al
            #destino.
            distOriginal=np.linalg.norm(Ship.pos-destino.pos)-0.01
        #Movemos cada uno de los cuerpos en el sistema.

        co = 0
        for body in movBody:
            #Aceleración del planeta
            if co==15 and np.linalg.norm(Earth.pos-body.pos)<Earth.radius:
                body.pos = Earth.pos + np.array([0,Earth.radius,0])
            else:
                body.mov(acel(body.pos),dt)
            co += 1


            if tiempo>=inicio:

                #Condicion para beneficiar a las trayectorías que ponen en
                #orbita a la nave sobre el destino.
                if (np.linalg.norm(Ship.pos-destino.pos) <
                   (destino.radius/Luna.radius)*5*destino.radius):
                   tiempoEnOrbita += 1

                #Si la distancia nave-destino es menor que 0.05 UA, se sale del
                #while y regresa el valor más cercano.
                if(np.linalg.norm(Ship.pos-
                                  destino.pos)==destino.radius+Ship.radius):
                    print(vx,vy,inicio,
                          np.linalg.norm(Ship.pos-destino.pos)/10 +
                                        (tiempo/100-tiempoEnOrbita)/tiempoLimite)
                    return (np.linalg.norm(Ship.pos-destino.pos)/10 +
                           (tiempo/100-tiempoEnOrbita)/tiempoLimite)

                #Si la nave se acerca mucho al Sol, se sale del while y regresa
                #un valor de penalización.
                if(np.linalg.norm(Ship.pos-Sun.pos)<0.5):
                    print(vx,vy,inicio,50)
                    return 50

        #Hacemos una lista con todas las distancias Nave-Destino.
        if tiempo>=inicio:
            posiciones.append(np.linalg.norm(Ship.pos-destino.pos))

        #Contador que se ocupa para saber cuando iniciar el viaje de la nave.
        tiempo+=1

        #Condición de finalización del while, evitar un ciclo infinito.
        if(tiempo==tiempoLimite):
            break

    #Acomodamos de menor a mayor las distancias nave-destino.
    posiciones.sort()

    #Si la menor distancia a la que la nave estuvo del destino es menor
    #que la distancia original(Tierra-destino), de la cual sale la nave
    if  posiciones[0]<distOriginal:
        print(vx,vy,inicio,
              np.linalg.norm(Ship.pos-destino.pos)/10 +
                             (tiempo/100-tiempoEnOrbita)/tiempoLimite)
        return posiciones[0]/10 + (tiempo/10-tiempoEnOrbita)/tiempoLimite

    print(vx,vy,inicio,
          np.linalg.norm(Ship.pos-destino.pos)/10 +
                        (tiempo/100-tiempoEnOrbita)/tiempoLimite)
    return (np.linalg.norm(Ship.pos-destino.pos)/10 +
           (tiempo/100-tiempoEnOrbita)/tiempoLimite)


"""Calcular aceleraciones para impedir divisiones entre cero"""
def acel(x):
    global movBody

    distancias = []
    for i in movBody:
        distancias.append(x-i.pos)

    a = np.array([0.0,0.0,0.0])
    j=0
    for i in movBody:
        norma = np.linalg.norm(distancias[j])
        if norma>0.0:
            a +=  i.mass * (distancias[j] / norma**3)
        j+=1

    return -G * a
