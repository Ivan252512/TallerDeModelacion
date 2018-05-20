from vpython import *
import math
import funciones

G= 39.478417
pi = 3.141592654
dospi=2*pi
pimedios=pi/2
rship=1.01
"""Mercurio"""
rmerc=0.38
mmerc=0.166e-6
vmerc=sqrt(G/rmerc)
wmerc=vmerc/rmerc

"""Venus"""
rvenus=0.723
mvenus=2.44e-6
vvenus=sqrt(G/rvenus)
wvenus=vvenus/rvenus

"""Marte"""
rmarte=1.53 #Distancia media al Sol del planeta de destino UA
mmarte=3.214e-7 #Masa del planeta de destino MS
vmarte=sqrt(G/rmarte)  #Velocidad de Marte
wmarte=vmarte/rmarte   # Velocidad angular de Marte

"""Jupiter"""
rjup=5.2
mjup=954.79e-6
vjup=sqrt(G/rjup)
wjup=vjup/rjup

"""Saturno"""
rsat=9.57
msat=285.88e-6
vsat=sqrt(G/rsat)
wsat=vsat/rsat

"""Urano"""
rur=19.3
mur=43.66e-6
vur=sqrt(G/rur)
wur=vur/rur

"""Neptuno"""
rnep=30.2
mnep=51.51e-6
vnep=sqrt(G/rnep)
wnep=vnep/rnep

"""Nave"""
vship=sqrt((2*G*rmarte)/rship/(rship+rmarte))  #Velocidad Inicial nave


ANG=pi
print('Posición angular inicial, ', ANG*180/pi)
sa = sin(ANG)
ca = cos(ANG)
sca = sin(pimedios+ANG)
cca = cos(pimedios+ANG)
Rmin=rmarte*(mmarte)**0.4

Sun = sphere(pos=vector(0,0,0),
             radius=0.1, color=color.yellow,make_trail=False, interval=10)
Sun.mass = 1
Sun.v = vector(0, 0, 0)

Earth = sphere(pos=vector(1,0,0),
               radius=0.01, color=color.blue,make_trail=False, interval=10)
Earth.mass = 3.004e-6
Earth.v = vector(0, 6.283, 0)

Mercury = sphere(pos=vector(rmerc*ca,rmerc*sa,0),
                 radius=0.005, color=color.red,make_trail=False, interval=10)
Mercury.mass = mmerc
Mercury.v = vector(vmerc*cca, vmerc*sca, 0)

Venus = sphere(pos=vector(rvenus*ca,rvenus*sa,0),
               radius=0.01, color=color.red,make_trail=False, interval=10)
Venus.mass = mvenus
Venus.v = vector(vvenus*cca, vvenus*sca, 0)

Mars = sphere(pos=vector(rmarte*ca,rmarte*sa,0),
              radius=0.01, color=color.red,make_trail=False, interval=10)
Mars.mass = mmarte
Mars.v = vector(vmarte*cca, vmarte*sca, 0)

Jupyter = sphere(pos=vector(rjup*ca,rjup*sa,0),
                 radius=0.07, color=color.green,make_trail=False, interval=10)
Jupyter.mass = mjup
Jupyter.v = vector(vjup*cca, vjup*sca, 0)

Saturn = sphere(pos=vector(rsat*ca,rsat*sa,0),
                radius=0.05, color=color.green,make_trail=False, interval=10)
Saturn.mass = msat
Saturn.v = vector(vsat*cca, vsat*sca, 0)

Uranus = sphere(pos=vector(rur*ca,rur*sa,0),
                radius=0.04, color=color.green,make_trail=False, interval=10)
Uranus.mass = mur
Uranus.v = vector(vur*cca, vur*sca, 0)

Neptune = sphere(pos=vector(rnep*ca,rnep*sa,0),
                 radius=0.04, color=color.green,make_trail=False, interval=10)
Neptune.mass = mnep
Neptune.v = vector(vnep*cca, vnep*sca, 0)

Ship = sphere(pos=vector(rship, 0, 0),
              radius=0.0001, color=color.orange,make_trail=True, interval=10)
Ship.mass = 3.214e-28
Ship.v = vector(0, vship, 0)

dt = 2.73785078e-4
print('Radio de influencia del planeta, ', Rmin)
flag=0


while True:
    rate(2000)
    for body in [Mercury,Venus,Earth,Mars,Jupyter,Saturn,Uranus,Neptune,Ship]:
        if body == Ship:
            DS=body.pos-Sun.pos
            DM=body.pos-Mercury.pos
            DV=body.pos-Venus.pos
            DT=body.pos-Earth.pos
            DMars=body.pos-Mars.pos
            DJ=body.pos-Jupyter.pos
            DSat=body.pos-Saturn.pos
            DU=body.pos-Uranus.pos
            DN=body.pos-Neptune.pos
            as1= -G*(Sun.mass*DS/mag(DS)**3+
                     Mercury.mass*DM/mag(DM)**3+
                     Venus.mass*DV/mag(DV)**3+
                     Earth.mass*DT/mag(DT)**3+
                     Mars.mass*DMars/mag(DMars)**3+
                     Jupyter.mass*DJ/mag(DJ)**3+
                     Saturn.mass*DSat/mag(DSat)**3+
                     Uranus.mass*DU/mag(DU)**3+
                     Neptune.mass*DN/mag(DN)**3)
            body.pos += body.v*dt + 0.5*as1*dt*dt
            body.v += as1*dt
        else:
            distance = body.pos - Sun.pos
            a1 = -G*Sun.mass*distance/mag(distance)**3
            body.pos += body.v*dt + 0.5*a1*dt*dt
            body.v += a1*dt
