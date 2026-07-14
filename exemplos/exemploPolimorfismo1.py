class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        print(f"{self.nome} emite um som genérico")
class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} late")
class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} Mia")

def fazer_barulho(animal):
    animal.emitir_som()

animais = [Cachorro("Tobi"), Gato("Pipi"), Cachorro("Rex"), Gato("Miau")]

for animal in animais:
    fazer_barulho(animal)