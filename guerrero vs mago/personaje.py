class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 7
        self.defensa = 3
        self.inventario = []

    def mostrarInfo(self):
        print(f"""Nombre: {self.nombre}
----------------------------
Vida: {self.vida}
-----------------
Ataque: {self.ataque}
-----------------
Defensa: {self.defensa}
-----------------
Inventario: Pocion(20-HP), Arma(5-ATK), Escudo(5-DEF)
-----------------------------------------------------
""")

    def atacar(self, otro_personaje):
        danio = self.ataque - otro_personaje.defensa
        if danio < 0:
            danio = 0
        otro_personaje.recibir_danio(danio)
        print("----------------------------------")
        print(f"¡{self.nombre} ha atacado haciendo {danio} DMG!")

    def recibir_danio(self, danio):
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
        print(f"Ahora {self.nombre} tiene {self.vida} HP")

    def agregar_item(self, item):
        self.inventario.append(item)
        print(f"¡{self.nombre} ha agregado {item}!")


