class ContaBancaria:
    def __init__(self, titular, numero, saldoInicial = 0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldoInicial

    #depositar
    def depositar(self, valor):
        if valor>0:
            self.saldo += valor
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso")
        else:
            print("valor de deposito inválido")
    #sacar
    def sacar(self, valor):
        if valor<=0:
            print("Valor de saque invalido")
        elif valor>self.saldo:
            print("Valor insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque deu certo com o valor de R$ {valor:.2f} realizado com sucesso")
    #fazer extrato
    def exibir_extrato(self):
        print("="*20)
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

conta1 = ContaBancaria("nome", "numero", 500)
conta1.depositar(300.00)
conta1.sacar(100.00)
conta1.exibir_extrato()

conta2 = ContaBancaria("Joao", "123-4", 400)
conta2.depositar(1000)
conta2.exibir_extrato()