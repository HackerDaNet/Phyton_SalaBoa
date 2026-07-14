class Lampada:
    def __init__(self, marca):
        self.marca = marca
    def acender(self):
        print(f"Lampada da marca: {self.marca} está acendendo")
class Incandecente(Lampada):
    def acender(self):
        print(f"Lampada da marca: {self.marca} esta acendendo com uma luz quente e amarelada")
class Fluorecente(Lampada):
    def acender(self):
        print(f"Lampada da marca: {self.marca} esta acendendo com uma luz fria e branca")
class Led(Lampada):
    def acender(self):
        print(f"Lampada da marca: {self.marca} esta acendendo com baixo consumo de energia")

def iniciar_lampadas(Lampada1):
    Lampada1.acender()

lampadas = [Incandecente("Webber"), Fluorecente("Kelvin"), Led("Enaldinho")]

for lampada in lampadas:
    iniciar_lampadas(lampada)