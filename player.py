import random

class Player():
    def __init__(self):
        self.health = random.randint(50, 100)        
        print("Player creado con health de" , self.health)

    def powerup(self):
        self.health += random.randint(10, 25)
        print("WOOOT!!!! El player ahora tiene" , self.health)

    def take_damage(self):
        self.health -= random.randint(10, 25)
        print("ARGHHHH!!!! El player toma daño ahora tiene " + str(self.health))
    
    def tell_health(self):
        print("Mi health en este momento es de " + str(self.health))


    
player1 = Player()
player1.powerup()
player1.take_damage()
player2 = Player()
player2.take_damage()
player2.powerup()
