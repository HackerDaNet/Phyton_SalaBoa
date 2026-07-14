class Funcionario:
    def __init__(self, forma, cor):
        self.forma = forma
        self.cor = cor

    def calcular_area(self):
        print("Sem valores para calcular área")
    def exibir_info(self):
        print(f"Cor: {self.cor}")
        print(f"Forma: {self.forma}")

#filha
class Circulo(Funcionario):
    def __init__(self, forma, cor, raio):
        super().__init__(forma, cor)
        self.raio = raio
    def calcular_area(self):
        print(f"Circulo: {self.raio * 3.14159}")

class Retangulo(Funcionario):
    def __init__(self, forma, cor, largura, altura):
        super().__init__(forma, cor)
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        print(f"Retangulo: {self.largura * self.altura}")
class Triangulo(Funcionario):
    def __init__(self, forma, cor, base, altura):
        super().__init__(forma, cor)
        self.base = base
        self.altura = altura
    def calcular_area(self):
        print(f"Triangulo: {self.base * self.altura}")
#uso
c= Circulo("Circulo", "Azul", 50)
c.calcular_area()
c.exibir_info()

r= Retangulo("Retangulo", "Vermelho", 50, 50)
r.calcular_area()
r.exibir_info()

t= Triangulo("Triangulo", "Vermelho", 30, 53)
t.calcular_area()
t.exibir_info()