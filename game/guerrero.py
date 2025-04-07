from personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.defensa += self.defensa * 1.05
        self.ataque -= 3