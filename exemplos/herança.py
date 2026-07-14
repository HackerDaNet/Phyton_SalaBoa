class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

class Funcionario:
    def calcular_salario(self):
        return self.salario_base

class Vendedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base + self.comissao