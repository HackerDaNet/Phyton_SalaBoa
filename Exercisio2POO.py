class Produto:
   total_cadastro = 0
   def __init__(self, largura, altura):
       self.largura = largura
       self.altura = altura

   def area(self, largura, altura):
        print(f"A área é: ", largura * altura)

   def perimetro(self, largura, altura):
       print(f"O perimetro é: " , (largura+altura)*2)

   def info(self, largura, altura):
       print(f"A largura é: ", largura, " A altura é: ", altura, " a área é: ", largura*altura, "O perimetro é: ", (largura+altura)*2)
p1=Produto(int(input("Qual a largura: ")), int(input("Qual a altura: ")))
p1.area(largura=p1.largura, altura=p1.altura)
p1.perimetro(largura=p1.largura, altura=p1.altura)

p1.info(largura=p1.largura, altura=p1.altura)
