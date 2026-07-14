class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: R$ {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-"*20)

#filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_de_portas):
        super().__init__(marca, modelo, ano)
        self.numero_de_portas = numero_de_portas
    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Numero de portas: {self.numero_de_portas}")
        print("-"*20)

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cilindradas: {self.cilindradas}")
        print("-"*20)
#uso
c= Carro("Pejo", "Pato", 2019, 4)
c.exibir_info()
m= Moto("Marca", "Modelo", 2020, 5)
m.exibir_info()