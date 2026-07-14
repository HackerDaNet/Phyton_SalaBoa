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
class Horista(Funcionario):
    def __init__(self, nome, salario_base, horas_trabalhadas, valor_hora):
        super().__init__(nome, salario_base)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

class Mensalista(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
#uso
h= Horista("Webber", 0, 38, 52)
h.calcular_salario()
h.exibir_info()

m=Mensalista("Enaldinho", 2500)
m.exibir_info()