class Estoques:
    def __init__(self, nome, valor, estoque):
        self.nome = nome
        self.valor = valor
        self.__estoque = estoque


    #GETTER
    def get_estoque(self):
        print(self.__estoque)
    def get_info(self):
        print(self.nome, self.valor, self.__estoque)
    #SETTER
    def depositar_estoque(self, depositar):
        self.__estoque = self.__estoque + depositar
    def retirar_estoque(self, extrair):
        self.__estoque = self.__estoque - extrair
a1 = Estoques("Mesa auruda", 300, 20)
a1.get_estoque()
a1.depositar_estoque(50)
a1.get_estoque()
a1.retirar_estoque(20)
a1.get_info()
a2 = Estoques("Cadeira auruda", 255, 25)
a2.get_estoque()
a2.depositar_estoque(50)
a2.get_estoque()
a2.retirar_estoque(25)
a2.get_info()