import cuerposCelestes as cc
import numpy as np


"""Es la función principal, descripción en el archivo .pdf adjunto"""
def f(vx,vy,inicio):

    G= 39.4784176 # AU³ YR⁻² SM-¹
    ANG= np.pi/2
    sa = np.sin(ANG)
    ca = np.cos(ANG)
    sca = np.sin(np.pi/2+ANG)
    cca = np.cos(np.pi/2+ANG)

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

    """Marte"""
    rmarte=1.53 #Distancia media al Sol del planeta de destino UA
    mmarte=3.214e-7 #Masa del planeta de destino MS
    vmarte=np.sqrt(G/rmarte)  #Velocidad de Marte
    wmarte=vmarte/rmarte   # Velocidad angular de Marte

    """Jupiter"""
    rjup=5.2
    mjup=954.79e-6 #-4
    vjup=np.sqrt(G/rjup)
    wjup=vjup/rjup

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

    Sun = cc.celestialBody(1.0, 1.0, np.array([0.0,0.0,0.0]),
                           np.array([0.0,0.0,0.0]))

    Mercury = cc.celestialBody(mmerc, 0.1, np.array([rmerc*ca, rmerc*sa,0]),
                               np.array([vmerc*cca, vmerc*sca, 0]))

    Venus = cc.celestialBody(mvenus, 0.1, np.array([rvenus*ca,rvenus*sa,0]),
                            np.array([vvenus*cca, vvenus*sca, 0]))

    Earth = cc.celestialBody(3.004e-6, 0.1, np.array([1.0,0.0,0.0]),
                             np.array([0.0,6.283,0.0]))

    Mars = cc.celestialBody(3.214e-7, 0.1, np.array([rmarte*ca,rmarte*sa,0]),
                            np.array([vmarte*cca, vmarte*sca, 0]))

    Jupyter = cc.celestialBody(mjup, 0.1, np.array([rjup*ca,rjup*sa,0]),
                            np.array([vjup*cca, vjup*sca, 0]))

    Saturn = cc.celestialBody(msat, 0.1, np.array([rsat*ca,rsat*sa,0]),
                            np.array([vsat*cca, vsat*sca, 0]))

    Uranus = cc.celestialBody(mur, 0.1, np.array([rur*ca,rur*sa,0]),
                                np.array([vur*cca, vur*sca, 0]))

    Neptune = cc.celestialBody(mnep, 0.1, np.array([rnep*ca,rnep*sa,0]),
                            np.array([vnep*cca, vnep*sca, 0]))

    Ship = cc.celestialBody(3.214e-28, 0.1, np.array([1.0,0.0,0.0]),
                            np.array([vx, vy, 0.0]))


    #Condición de penalización para que la rapidez de la nave no supere el
    #límite impuesto.
    if(np.sqrt(vx**2+vy**2)>7.5):
        #Imprime los valores a evaluar y su resultado.
        print(vx,vy,inicio,10000)
        return 10000

    #Diferencial a usar
    dt = 2.73785078e-4
    tiempo=0
    posiciones=[]
    #Primer distancia Nave-destino, se usa abajo, se le resta un poco a
    #conveniencia, para lograr que las trayectorias se encaminen al destino.
    distOriginal=np.linalg.norm(Ship.pos-Neptune.pos)-0.1
    while True:
        #Tiempo inicial del viaje de la nave, es decir, la nave puede iniciar
        #su trayectoria mucho después de que se inicie la simulación.
        if tiempo==inicio:
            #cambiamos la posición inicial de la nave a la actual de la Tierra.
            Ship.pos=np.array(Earth.pos[:])
        #Movemos cada uno de los cuerpos en el sistema.
        for body in [Mercury, Venus, Earth, Mars, Jupyter, Saturn, Uranus,
                     Neptune, Ship]:
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
                as1= -G*(Sun.mass*DS/np.linalg.norm(DS)**3+
                         Mercury.mass*DM/np.linalg.norm(DM)**3+
                         Venus.mass*DV/np.linalg.norm(DV)**3+
                         Earth.mass*DT/np.linalg.norm(DT)**3+
                         Mars.mass*DMars/np.linalg.norm(DMars)**3+
                         Jupyter.mass*DJ/np.linalg.norm(DJ)**3+
                         Saturn.mass*DSat/np.linalg.norm(DSat)**3+
                         Uranus.mass*DU/np.linalg.norm(DU)**3+
                         Neptune.mass*DN/np.linalg.norm(DN)**3)
                #Actualización de la velocidad y posición de la nave.
                body.mov(as1, dt)
                """A partir de aquí se define el destino (Marte por default),
                si se quiere cambiar el destino solo cambie Neptune.pos por otro
                planeta (e.g para Júpiter sería Jupyter.pos)"""
                #Si la distance nave-destino es menor que 0.05 UA, se sale del
                #while y regresa el valor más cercano.
                if(np.linalg.norm(Ship.pos-Neptune.pos)<0.05):
                    print(vx,vy,inicio,np.linalg.norm(Ship.pos-Neptune.pos))
                    return np.linalg.norm(Ship.pos-Neptune.pos)
                #Si la nave se acerca mucho al Sol, se sale del while y regresa
                #un valor de penalización.
                if(np.linalg.norm(Ship.pos-Sun.pos)<0.5):
                    print(vx,vy,inicio,5000)
                    return 5000
            #Movimiento de cada uno de los planetas
            #Si se cambia el destino no se debe cambiar nada en este elif
            elif body!=Ship:
                #Distancia Sol-planeta
                distance = body.pos - Sun.pos
                #Aceleración del planeta
                a1 = -G*Sun.mass*distance/np.linalg.norm(distance)**3
                #de la velocidad y posición del planeta.
                body.mov(a1, dt)
        #Hacemos una lista con todas las distancias Nave-Destino.
        posiciones.append(np.linalg.norm(Ship.pos-Neptune.pos))
        #Contador que se ocupa para saber cuando iniciar el viaje de la nave.
        tiempo+=1
        #Condición de finalización del while, evitar un ciclo infinito.
        if(tiempo==500000):
            break
        #Acomodamos de menor a mayor las distancias nave-destino.
        posiciones.sort()
        #Si la menor distancia a la que la nave estuvo del destino es menor
        #que la distancia original(Tierra-destino), de la cual sale la nave
    if  posiciones[0]<distOriginal:
        print(vx,vy,inicio,np.linalg.norm(Ship.pos-Neptune.pos))
        return posiciones[0]
    print(vx,vy,inicio,np.linalg.norm(Ship.pos-Neptune.pos))
    return np.linalg.norm(Ship.pos-Neptune.pos)
