class Relogio:
    def __init__(self, segundos, minutos, horas):
        self.__segundos = segundos
        self.__minutos = minutos
        self.__horas = horas


    #GETTER
    def get_hora(self):
        print(self.__horas, self.__minutos, self.__segundos)
    #SETTER
    def trocar_horas(self, depositar):
        if 0 < self.__horas < 24:
            self.__horas = depositar
        else:
            print("Horas insuficientes")
    def trocar_minutos(self, extrair):
        if 0 < self.__minutos < 60:
            self.__minutos = extrair
        else:
            print("Minutos insuficientes")
    def trocar_segundos(self, alto):
        if 0 < self.__segundos < alto:
            self.__segundos = alto
        else:
            print("Segundos insuficientes")
    def avancar1segundo(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos == 60:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas == 24:
                    self.__horas = 0
                else:
                    print(self.__horas, self.__minutos, self.__segundos)
            else:
                print(self.__horas, self.__minutos, self.__segundos)
        else:
            print(self.__horas, self.__minutos, self.__segundos)

a1 = Relogio(20, 20, 20)
a1.get_hora()
a1.trocar_horas(23)
a1.trocar_minutos(59)
a1.trocar_segundos(59)
a1.get_hora()
a1.avancar1segundo()
a1.get_hora()
a2 = Relogio(22, 33, 22)
a2.get_hora()
a2.trocar_horas(25)
a2.get_hora()