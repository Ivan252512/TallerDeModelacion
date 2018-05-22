"""Busqueda de la orbita óptima usando el algoritmo genético"""
import ag
import math
import numpy as np
import matplotlib.pyplot as plt

G= 39.4784176 # AU⁻³ YR⁻² SM-¹
pi = 3.141592654
dospi=2*pi
pimedios=pi/2
rship=1.01
"""Mercurio"""
rmerc=0.38
mmerc=0.166e-6
vmerc=math.sqrt(G/rmerc)
wmerc=vmerc/rmerc

"""Venus"""
rvenus=0.723
mvenus=2.44e-6
vvenus=math.sqrt(G/rvenus)
wvenus=vvenus/rvenus

"""Marte"""
rmarte=1.53 #Distancia media al Sol del planeta de destino UA
mmarte=3.214e-7 #Masa del planeta de destino MS
vmarte=math.sqrt(G/rmarte)  #Velocidad de Marte
wmarte=vmarte/rmarte   # Velocidad angular de Marte

"""Jupiter"""
rjup=5.2
mjup=954.79e-6
vjup=math.sqrt(G/rjup)
wjup=vjup/rjup

"""Saturno"""
rsat=9.57
msat=285.88e-6
vsat=math.sqrt(G/rsat)
wsat=vsat/rsat

"""Urano"""
rur=19.3
mur=43.66e-6
vur=math.sqrt(G/rur)
wur=vur/rur

"""Neptuno"""
rnep=30.2
mnep=51.51e-6
vnep=math.sqrt(G/rnep)
wnep=vnep/rnep

ANG=pi/2

sa = math.sin(ANG)
ca = math.cos(ANG)
sca = math.sin(pimedios+ANG)
cca = math.cos(pimedios+ANG)


def f(vx,vy,inicio):
    print("+")
    limite=1000000
    SunPos=np.array([0.0,0.0,0.0])
    MercuryPos=np.array([rmerc*ca,rmerc*sa,0.0])
    VenusPos=np.array([rvenus*ca,rvenus*sa,0.0])
    EarthPos=np.array([1.0,0.0,0.0])
    MarsPos=np.array([rmarte*ca,rmarte*sa,0.0])
    JupyterPos=np.array([rjup*ca,rjup*sa,0.0])
    SaturnPos=np.array([rsat*ca,rsat*sa,0.0])
    UranusPos=np.array([rur*ca,rur*sa,0.0])
    NeptunePos=np.array([rnep*ca,rnep*sa,0.0])
    NavePos=np.array([1.01,0.0,0.0])

    MercuryVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    VenusVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    EarthVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    MarsVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    JupyterVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    SaturnVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    UranusVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    NeptuneVel=np.array([vmerc*cca, vmerc*sca, 0.0])
    NaveVel=np.array([vx,vy,0])

    Planetas=[[MercuryPos,MercuryVel],[VenusPos,VenusVel],[EarthPos,EarthVel],
              [MarsPos,MarsVel],[JupyterPos,JupyterVel],[SaturnPos,SaturnVel],
              [UranusPos,UranusVel],[NeptunePos,NeptuneVel]]
    dt = 2.73785078e-4
    cont=0
    tiempo=0
    while True:
        if cont==inicio:
            NavePos=EarthPos
        if cont>=inicio:
            DS=NavePos-SunPos
            DM=NavePos-MercuryPos
            DV=NavePos-VenusPos
            DT=NavePos-EarthPos
            DMars=NavePos-MarsPos
            DJ=NavePos-JupyterPos
            DSat=NavePos-SaturnPos
            DU=NavePos-UranusPos
            DN=NavePos-NeptunePos
            as1= -G*(DS/np.linalg.norm(DS)**3+
                     mmerc*DM/np.linalg.norm(DM)**3+
                     mvenus*DV/np.linalg.norm(DV)**3+
                     (3.004e-6)*DT/np.linalg.norm(DT)**3+
                     mmarte*DMars/np.linalg.norm(DMars)**3+
                     mjup*DJ/np.linalg.norm(DJ)**3+
                     msat*DSat/np.linalg.norm(DSat)**3+
                     mur*DU/np.linalg.norm(DU)**3+
                     mnep*DN/np.linalg.norm(DN)**3)
            NavePos+= NaveVel*dt + 0.5*as1*dt*dt
            NaveVel += as1*dt
            tiempo+=1
        for i in Planetas:
            distance = i[0] - SunPos
            a1 = -G*distance/np.linalg.norm(distance)**3
            i[0] +=i[1]*dt + 0.5*a1*dt*dt
            i[1] += a1*dt
        cont+=1
        if (np.linalg.norm(NavePos-JupyterPos)<0.01):
            break
        if (np.linalg.norm(NavePos-SunPos)<1):
            tiempo=limite*10
            break
        if(cont>=limite):
            tiempo=limite*10
            break
    return tiempo

optimo=ag.evolucion(f,0,10,1000000,ag.poblacion(100,20),ag.poblacion(100,20),
                    ag.poblacion(100,20),25)
print(optimo)
