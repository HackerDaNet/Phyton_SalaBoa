class Produto:
   total_cadastro = 0
   def __init__(self, marca, modelo, ano=0, velocidade=0):
       self.marca = marca
       self.modelo = modelo
       self.ano = ano
       self.velocidade = velocidade
   def info(self, marca, modelo, ano, velocidade):
        print(f"Olá minha marca é : : {self.marca}")
        print(f" eu sou do modelo: :{self.modelo}")
        print(f" eu sou do ano: :{self.ano}")
        print(f" eu estou na velocidade :{self.velocidade} km/h")
   def acelerar(self, velocidade):
        print("Quanto quer acelerar?")
        velocidade1 = int(input())
        p1.velocidade = velocidade+velocidade1
        print(p1.velocidade)

   def desacelerar(self, velocidade):
       print("Quanto quer desacelerar?")
       velocidade2 = int(input())
       p1.velocidade = velocidade-velocidade2
       print(p1.velocidade)
p1=Produto((input("Qual é a marca: ")), (input("Qual o modelo: ")), int(input("Qual a ano: ")), int(input("Qual a velocidade: ")))

p1.acelerar(p1.velocidade)
p1.desacelerar(p1.velocidade)