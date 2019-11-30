import random

class Baraja():
    def __init__(self):
        trajes = ["Espadas", "Corazones", "Diamantes", "Treboles"]
        rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "As", "Comodin", "Rey", "Reina"] 

        # baraja de 52 cartas disponible.
        self.barajas = []

        # ciclo for para cada traje en trajes
        for traje in trajes:
            # ciclo for para cada rango en rangos
            for rango in rangos:
                # concatena el rango y el traje y 
                # append a self.barajas()
                self.barajas.append(rango + " de " + traje)

    def barajear(self):
        # barajea self.barajas
        random.shuffle(self.barajas)

    def repartir(self):
        # regresar una carta random
        print(self.barajas.pop())        

mi_baraja = Baraja()
mi_baraja.barajear()
mi_baraja.repartir()
mi_baraja.repartir()
mi_baraja.repartir()
mi_baraja.repartir()
