class Termometro:
    def __init__(self, temperatura):
        self.__temperatura = temperatura


    #GETTER
    def get_valor(self):
        print(self.__temperatura)
    #SETTER
    def trocar_temperatura(self, trocar):
        if 16<=trocar<=30:
            self.__temperatura = trocar
        else:
            print("Valor não pode ser menor que 16 e maior que 30")

a1 = Termometro(20)
a1.trocar_temperatura(16)
a1.get_valor()
a2 = Termometro(30)
a2.trocar_temperatura(41)
a2.get_valor()