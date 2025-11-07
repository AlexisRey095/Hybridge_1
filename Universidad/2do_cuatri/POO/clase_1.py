class arma:
    def __init__(self, nombre, damage):
        self.nombre = nombre
        self.damage = damage

    def atacar(self):
        print(f'el arma {self.nombre} hace un daño de {self.damage}')
        return self.damage

#Tipos de armas ----------------------------------------

espada = arma(nombre='Espada', damage=10)
arco = arma(nombre='Arco', damage=12)
hacha = arma(nombre='Hacha', damage=28)
baston = arma(nombre='Baston', damage=32)

#Personajes --------------------------------------------

class Personaje:
    def __init__(self, nombre, vida, tipo_arma):
        self.nombre = nombre
        self.vida = vida
        self.arma = tipo_arma

    def Mostrar_Stats(self):
        print(f'nombre:  {self.nombre}')
        print(f'vida:  {self.vida}')
        print(f'arma:  {self.arma.nombre}')

    def atacar(self):
        return self.arma.atacar()

jugador_1 = Personaje(nombre='Alexis', vida=20, tipo_arma=arco)
jugador_1.Mostrar_Stats()
jugador_2 = Personaje(nombre='Bob', vida=10, tipo_arma=espada)
jugador_2.Mostrar_Stats()