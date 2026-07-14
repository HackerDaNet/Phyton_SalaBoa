class Banco:
    def __init__(self, nome, valor):
        self.nome = nome
        self.__valor = valor


    #GETTER
    def get_valor(self):
        print(self.__valor)
    #SETTER
    def depositar_valor(self, depositar):
        self.__valor = self.__valor + depositar
    def retirar_valor(self, extrair):
        self.__valor = self.__valor - extrair
a1 = Banco("Carlos", 300)
a1.get_valor()
a1.depositar_valor(200)
a1.get_valor()
a1.retirar_valor(150)
a2 = Banco("Joao", 400)
a2.get_valor()
a2.retirar_valor(300)
a2.depositar_valor(250)
a2.get_valor()