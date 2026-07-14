class Transporte:
    def __init__(self, nome):
        self.nome = nome
    def cumprimentar(self):
        print(f"Olá, eu sou o {self.nome}, prazer. ")
class Recepcionista(Transporte):
    def cumprimentar(self):
        print(f"Olá eu sou o {self.nome}, prazer. Sou o recepcionista desta unidade. ")
class Gerente(Transporte):
    def cumprimentar(self):
        print(f"Olá, eu sou o {self.nome}, prazer. Sou o gerente desta unidade.")
class Tecnico(Transporte):
 def cumprimentar(self):
     print(f"Olá eu sou o {self.nome}, prazer. Eu sou o técnico desta unidade.")

def iniciar_cumprimentos(Cumprimentar):
    Cumprimentar.cumprimentar()

cumprimentos = [Recepcionista("Enaldinho"), Tecnico("Webber"), Gerente("ADM")]

for cumprimentar in cumprimentos:
    iniciar_cumprimentos(cumprimentar)