import random

class Dado():
    def __init__(self, caras):
        self.caras = caras

    def tirar(self):
        return random.randint(1, self.caras)


dado_de_6_lados = Dado(6)
dado_de_12_lados = Dado(12)
dado_de_24_lados = Dado(24)

print(dado_de_6_lados.tirar())
print(dado_de_12_lados.tirar())
print(dado_de_24_lados.tirar())
