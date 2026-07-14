class Produto:
    save = []
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def soma (self):
        self.save.append(f"Somar: {self.A} - {self.B} = {self.A + self.B}")
        return (self.A + self.B)

    def subtracao(self):
        self.save.append(f"Subtrair: {self.A} - {self.B} = {self.A - self.B}")
        return (self.A - self.B)

    def multiplicacao(self):
        self.save.append(f"Multiplicar: {self.A} * {self.B} = {self.A * self.B}")
        return (self.A * self.B)

    def divisao(self):
        if self.B != 0:
            self.save.append(f"Dividir: {self.A} / {self.B} = {self.A / self.B}")
            return (self.A / self.B)
        else:
            self.save.append(f"Divisão: {self.A} / {self.B} = Não pode dividir por 0 man")
            return "Deu ruim, tentou dividir por 0"

    def exibir_historico(self):
        print("Save do historico de operações:")
        for operacao in self.save:
            print(operacao)


calculadora1 = Produto(70, 15)
calculadora1.soma()
calculadora1.subtracao()
calculadora1.multiplicacao()
calculadora1.divisao()
calculadora1.exibir_historico()