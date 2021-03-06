"""Función de evaluación"""

#vpython es una librería para visualización gráfica.
from vpython import *

"""Es la función principal, descripción en el archivo .pdf adjunto"""
def f(vx,vy,inicio):
    #Condición de penalización para que la rapidez de la nave no supere el
    #límite impuesto.
    if(sqrt(vx**2+vy**2)>7.5):
        #Imprime los valores a evaluar y su resultado.
        print(vx,vy,inicio,10000)
        return 10000
    #Herramientas de visual python para la visualización
    scene.width = 1400
    scene.height = 700
    scene.title = "Trayectorias óptimas en el Sistema Solar"
    scene.range = 36

    #Constantes y condiciones iniciales.
    G= 39.4784176 # AU³ YR⁻² SM-¹
    pi = 3.141592654
    dospi=2*pi
    pimedios=pi/2
    rship=1.01
    """Mercurio"""
    rmerc=0.38          #radio
    mmerc=0.166e-6      #masa
    vmerc=sqrt(G/rmerc) #velocidad tangencial
    wmerc=vmerc/rmerc   #velocidad angular

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
    mjup=954.79e-6 #-4
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
    condicionesIniciales=[vx, vy, inicio]
    vship=vector(condicionesIniciales[0], condicionesIniciales[1],0)
    ANG=pi/2

    #Ángulos para trabajar en coordenadas polares
    sa = sin(ANG)
    ca = cos(ANG)
    sca = sin(pimedios+ANG)
    cca = cos(pimedios+ANG)

    #Generación de objetos a representar con su posición, masa y velocidad.
    Sun = sphere(pos=vector(0,0,0),
                 radius=0.5, color=color.yellow,make_trail=False, interval=10)
    Sun.mass = 1
    Sun.v = vector(0, 0, 0)

    Earth = sphere(pos=vector(1,0,0),
                   radius=0.1, color=color.blue,make_trail=False, interval=10)
    Earth.mass = 3.004e-6
    Earth.v = vector(0, 6.283, 0)

    Mercury = sphere(pos=vector(rmerc*ca,rmerc*sa,0),
                     radius=0.05, color=color.orange,make_trail=False, interval=10)
    Mercury.mass = mmerc
    Mercury.v = vector(vmerc*cca, vmerc*sca, 0)

    Venus = sphere(pos=vector(rvenus*ca,rvenus*sa,0),
                   radius=0.1, color=color.yellow,make_trail=False, interval=10)
    Venus.mass = mvenus
    Venus.v = vector(vvenus*cca, vvenus*sca, 0)

    Mars = sphere(pos=vector(rmarte*ca,rmarte*sa,0),
                  radius=0.1, color=color.red,make_trail=False, interval=10)
    Mars.mass = mmarte
    Mars.v = vector(vmarte*cca, vmarte*sca, 0)

    Jupyter = sphere(pos=vector(rjup*ca,rjup*sa,0),
                     radius=0.3, color=color.orange,make_trail=False, interval=10)
    Jupyter.mass = mjup
    Jupyter.v = vector(vjup*cca, vjup*sca, 0)

    Saturn = sphere(pos=vector(rsat*ca,rsat*sa,0),
                    radius=0.25, color=color.cyan,make_trail=False, interval=10)
    Saturn.mass = msat
    Saturn.v = vector(vsat*cca, vsat*sca, 0)

    Uranus = sphere(pos=vector(rur*ca,rur*sa,0),
                    radius=0.2, color=color.blue,make_trail=False, interval=10)
    Uranus.mass = mur
    Uranus.v = vector(vur*cca, vur*sca, 0)

    Neptune = sphere(pos=vector(rnep*ca,rnep*sa,0),
                     radius=0.2, color=color.blue,make_trail=False, interval=10)
    Neptune.mass = mnep
    Neptune.v = vector(vnep*cca, vnep*sca, 0)

    Ship = sphere(pos=vector(rship, 0, 0), radius=0.00001,
                  color=color.orange,make_trail=False, interval=10)
    Ship.mass = 3.214e-28
    Ship.v = vector(vx, vy, 0.0)


    #Diferencial a usar
    dt = 2.73785078e-4
    tiempo=0
    posiciones=[]
    #Primer distancia Nave-destino, se usa abajo, se le resta un poco a
    #conveniencia, para lograr que las trayectorias se encaminen al destino.
    distOriginal=mag(Ship.pos-Mars.pos)-0.1
    while True:
        #Rapidez a la que se quiere visualizar cada iteración, no necesario.
        #rate(1000000000000)
        #Tiempo inicial del viaje de la nave, es decir, la nave puede iniciar
        #su trayectoria mucho después de que se inicie la simulación.
        if tiempo==inicio:
            #cambiamos la posición inicial de la nave a la actual de la Tierra.
            Ship.pos=Earth.pos
            #Efecto visual para que la trayectoria de la nave sea una linea.
            Ship.make_trail=True
        #Movemos cada uno de los cuerpos en el sistema.
        for body in [Mercury,Venus,Earth,Mars,Jupyter,Saturn,Uranus,Neptune,Ship]:
            #primero la nave
            if body == Ship and tiempo>=inicio:
                #Vectores de distancias entre los planetas, el Sol y la nave.
                DS=body.pos-Sun.pos
                DM=body.pos-Mercury.pos
                DV=body.pos-Venus.pos
                DT=body.pos-Earth.pos
                DMars=body.pos-Mars.pos
                DJ=body.pos-Jupyter.pos
                DSat=body.pos-Saturn.pos
                DU=body.pos-Uranus.pos
                DN=body.pos-Neptune.pos
                #Acelración de la nave
                as1= -G*(Sun.mass*DS/mag(DS)**3+
                         Mercury.mass*DM/mag(DM)**3+
                         Venus.mass*DV/mag(DV)**3+
                         Earth.mass*DT/mag(DT)**3+
                         Mars.mass*DMars/mag(DMars)**3+
                         Jupyter.mass*DJ/mag(DJ)**3+
                         Saturn.mass*DSat/mag(DSat)**3+
                         Uranus.mass*DU/mag(DU)**3+
                         Neptune.mass*DN/mag(DN)**3)
                #Actualización de la velocidad y posición de la nave.
                body.pos += body.v*dt + 0.5*as1*dt*dt
                body.v += as1*dt
                """A partir de aquí se define el destino (Marte por default),
                si se quiere cambiar el destino solo cambie Mars.pos por otro
                planeta (e.g para Júpiter sería Jupyter.pos)"""
                #Si la distance nave-destino es menor que 0.05 UA, se sale del
                #while y regresa el valor más cercano.
                if(mag(Ship.pos-Mars.pos)<0.05):
                    print(vx,vy,inicio,mag(Ship.pos-Mars.pos))
                    return mag(Ship.pos-Mars.pos)
                #Si la nave se acerca mucho al Sol, se sale del while y regresa
                #un valor de penalización.
                if(mag(Ship.pos-Sun.pos)<0.5):
                    print(vx,vy,inicio,5000)
                    return 5000
            #Movimiento de cada uno de los planetas
            #Si se cambia el destino no se debe cambiar nada en este elif
            elif body!=Ship:
                #Distancia Sol-planeta
                distance = body.pos - Sun.pos
                #Aceleración del planeta
                a1 = -G*Sun.mass*distance/mag(distance)**3
                #de la velocidad y posición del planeta.
                body.pos += body.v*dt + 0.5*a1*dt*dt
                body.v += a1*dt
        #Hacemos una lista con todas las distancias Nave-Destino.
        posiciones.append(mag(Ship.pos-Mars.pos))
        #Contador que se ocupa para saber cuando iniciar el viaje de la nave.
        tiempo+=1
        #Condición de finalización del while, evitar un ciclo infinito.
        if(tiempo==10000):
            break
        #Acomodamos de menor a mayor las distancias nave-destino.
        posiciones.sort()
        #Si la menor distancia a la que la nave estuvo del destino es menor
        #que la distancia original(Tierra-destino), de la cual sale la nave
    if  posiciones[0]<distOriginal:
        print(vx,vy,inicio,mag(Ship.pos-Mars.pos))
        return posiciones[0]
    print(vx,vy,inicio,mag(Ship.pos-Mars.pos))
    return mag(ship.pos-Mars.pos)
