class Animal:
    def __init__(self, especie):
        self.especie = especie
    def hablar(self):
        print('Hace un sonido')

class Gato(Animal):
    def hablar(self):
        print('MIAU')
