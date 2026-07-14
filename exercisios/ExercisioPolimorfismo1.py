class Transporte:
    def __init__(self, nome):
        self.nome = nome
    def viajar(self):
        print(f"{self.nome} Viajando...")
class Navio(Transporte):
    def viajar(self):
        print(f"{self.nome} Viajando de barco...")
class Aviao(Transporte):
    def viajar(self):
        print(f"{self.nome} Viajando de aviao...")
class Carro(Transporte):
 def viajar(self):
     print(f"{self.nome} Viajando de carro...")

def iniciar_viagem(Transporte):
    Transporte.viajar()

viagens = [Navio("Enaldinho"), Aviao("Webber"), Carro("Kelvin")]

for viagem in viagens:
    iniciar_viagem(viagem)