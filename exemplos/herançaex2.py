class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base
    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.calcular_salario():.2f}")
        print("-"*20)

#filha
class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)
        self.comissao = comissao
    def calcular_salario(self):
        return self.salario_base + self.comissao

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    def calcular_salario(self):
        return self.bonus + self.salario_base
#uso
f= Funcionario("joao", 2000)
v= Vendedor("Maria", 1800, 500)
g= Gerente("Carlos", 5600, 20000)

f.exibir_info()
v.exibir_info()
g.exibir_info()