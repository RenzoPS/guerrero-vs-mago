class Item:
    def __init__(self, nombre, tipo, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor

    def usar(self, personaje):
        if self.tipo == "Pocion":
            personaje.vida += self.valor
            if personaje.vida > 100:
                personaje.vida = 100
                print("(Vida maxima 100 HP)")
            print(f"""¡{personaje.nombre} ha usado una {self.nombre}!
Recupera {self.valor}PTS y ahora tiene {personaje.vida} HP""")
        elif self.tipo == "Arma":
            personaje.ataque += self.valor
            print(f"""¡{personaje.nombre} ha usado un {self.nombre}!
Aumenta {self.valor}PTS y ahora tiene {personaje.ataque} DMG""")
        elif self.tipo == "Escudo":
            personaje.defensa += self.valor
            print(f"""¡{personaje.nombre} ha usado un {self.nombre}!
Aumenta {self.valor}PTS y ahora tiene {personaje.defensa} DEF""")
