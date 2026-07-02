class Produto:
   total_cadastro = 0
   def __init__(self, nome, idade, cidade):
       self.nome = nome
       self.idade = idade
       self.cidade = cidade
   def info(self, nome, cidade, idade):
        print(f"Olá meu nome é: : {self.nome}")
        print(f" eu moro na cidade: :{self.cidade}")
        print(f" eu tenho: :{self.idade} anos.")


print("Qual seu nome?")
Produto.nome = input()

print("Qual sua idade?")
Produto.idade = input()

print("Qual sua cidade?")
Produto.cidade = input()

Produto.info(self=Produto, nome=Produto.nome, cidade=Produto.cidade, idade=Produto.idade)