#vpython es una librería para visualización gráfica.
from vpython import *

"""Es la función principal, descripción en el archivo .pdf adjunto"""
def f(vx,vy,inicio):

    scene.width = 1400
    scene.height = 700
    scene.title = "Trayectorias óptimas en el Sistema Solar"
    scene.range = 10

    G= 39.4784176 # AU³ YR⁻² SM-¹
    rmarte=1.53 #Distancia media al Sol del planeta de destino UA
    vmarte=sqrt(G/rmarte)  #Velocidad de Marte
    ANG= pi/2
    sa = sin(ANG)
    ca = cos(ANG)
    sca = sin(pi/2+ANG)
    cca = cos(pi/2+ANG)

    Sun = sphere(pos=vector(0,0,0),
                 radius=0.1, color=color.yellow,make_trail=False, interval=10)
    Sun.mass = 1
    Sun.v = vector(0, 0, 0)

    Earth = sphere(pos=vector(1.0,0.0,0.0),
                 radius=0.1, color=color.blue,make_trail=False, interval=10)
    Earth.mass = 3.004e-6
    Earth.v = vector(0.0,6.283,0.0)

    Mars = sphere(pos=vector(rmarte*ca,rmarte*sa,0),
                  radius=0.1, color=color.red,make_trail=False, interval=10)
    Mars.mass = 3.214e-7
    Mars.v = vector(vmarte*cca, vmarte*sca, 0)

    Ship = sphere(pos=vector(1, 0, 0), radius=0.00001,
                  color=color.orange,make_trail=False, interval=10)
    Ship.mass = 3.214e-28
    Ship.v = vector(vx, vy, 0.0)


    #Condición de penalización para que la rapidez de la nave no supere el
    #límite impuesto.
    if(sqrt(vx**2+vy**2)>7.5):
        #Imprime los valores a evaluar y su resultado.
        print(vx,vy,inicio,10000)
        return 10000

    #Diferencial a usar
    dt = 2.73785078e-4
    tiempo=0
    posiciones=[]
    #Primer distancia Nave-destino, se usa abajo, se le resta un poco a
    #conveniencia, para lograr que las trayectorias se encaminen al destino.
    distOriginal=mag(Ship.pos-Mars.pos)-0.1
    while True:
        #Tiempo inicial del viaje de la nave, es decir, la nave puede iniciar
        #su trayectoria mucho después de que se inicie la simulación.
        if tiempo==inicio:
            #cambiamos la posición inicial de la nave a la actual de la Tierra.
            Ship.pos=Earth.pos
            #Efecto visual para que la trayectoria de la nave sea una linea.
            Ship.make_trail=True
        #Movemos cada uno de los cuerpos en el sistema.
        for body in [Earth, Mars, Ship]:
            #primero la nave
            if body == Ship and tiempo>=inicio:
                #Vectores de distancias entre los planetas, el Sol y la nave.
                DS=body.pos-Sun.pos
                DT=body.pos-Earth.pos
                DMars=body.pos-Mars.pos
                #Acelración de la nave
                as1= -G*(Sun.mass*DS/mag(DS)**3+
                         Earth.mass*DT/mag(DT)**3+
                         Mars.mass*DMars/mag(DMars)**3)
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
    return mag(Ship.pos-Mars.pos)

print(f(6.8707317073170735, 0.6998998641012797, 1096.0 ))
