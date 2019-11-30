class Coche:
    """Abstraccion de los objetos coche."""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")

ford = Coche(3)
ford.arrancar()
ford.conducir()
ford.conducir()
ford.conducir()
ford.arrancar()
ford.conducir()
ford.cargar(3)
ford.arrancar()
ford.conducir()