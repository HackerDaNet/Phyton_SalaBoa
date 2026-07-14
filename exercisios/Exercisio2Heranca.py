class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):
        print(f"Saldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, rendimento):
        super().__init__(titular, saldo)
        self.rendimento = rendimento

    def render(self):
        self.saldo *= (1 + self.rendimento)
        print(self.saldo)


class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Não se pode depositar valores negativos")

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(self.saldo)
        else:
            print("Não pode sacar nada acima do limite")
cpou= ContaPoupanca("Civil", 100, 125)
cpou.exibir_saldo()
cpou.render()
cpou.depositar(50)
cpou.exibir_saldo()

cc = ContaCorrente("Militar", 180, 120)
cc.exibir_saldo()
cc.depositar(51)
cc.sacar(32)
cc.exibir_saldo()