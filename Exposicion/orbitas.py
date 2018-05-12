from vpython import *
import math

G= 39.4784176
pi = 3.141592654
dospi=2*pi
pimedios=pi/2
rship=1.01
rmarte=1.53 #Distancia media al Sol del planeta de destino UA
mmarte=3.214e-7 #Masa del planeta de destino MS


vmarte=sqrt(G/rmarte)  #Velocidad de Marte
wmarte=vmarte/rmarte   # Velocidad angular de Marte
vship=sqrt((2*G*rmarte)/rship/(rship+rmarte))*1.5  #Velocidad Inicial nave
a=(rship+rmarte)*0.5
T=a**1.5
ANG=pi-wmarte*T/2

print('Posición angular inicial, ', ANG*180/pi)
sa = sin(ANG)
ca = cos(ANG)
sca = sin(pimedios+ANG)
cca = cos(pimedios+ANG)
Rmin=rmarte*(mmarte)**0.4

Sun = sphere(pos=vector(0,0,0), radius=0.05, color=color.yellow,make_trail=True, interval=10)
Sun.mass = 1
Sun.v = vector(0, 0, 0)
Earth = sphere(pos=vector(1,0,0), radius=0.03, color=color.blue,make_trail=True, interval=10)
Earth.mass = 3.004e-6
Earth.v = vector(0, 6.283, 0)
Mars = sphere(pos=vector(rmarte*ca,rmarte*sa,0), radius=0.03, color=color.red,make_trail=True, interval=10)
Mars.mass = mmarte
Mars.v = vector(vmarte*cca, vmarte*sca, 0)
Ship = sphere(pos=vector(rship, 0, 0), radius=0.01, color=color.orange,make_trail=True, interval=10)
Ship.mass = 3.214e-28
Ship.v = vector(0, vship, 0)
dt = 2.73785078e-4
print('Radio de influencia del planeta, ', Rmin)
flag=0


while True:
    rate(500)
    for body in [Earth,Mars,Ship]:
        if body == Ship:
            DM=body.pos-Mars.pos
            DS=body.pos-Sun.pos
            if mag(DM)>Rmin:
                as1= -G*Sun.mass*DS/mag(DS)**3 #Importante
                body.pos += body.v*dt + 0.5*as1*dt*dt
                DS=body.pos-Sun.pos
                as2= -G*Sun.mass*DS/mag(DS)**3
                body.v += 0.5*(as1 + as2)*dt
