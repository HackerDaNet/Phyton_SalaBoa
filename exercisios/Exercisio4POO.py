class Produto:
   total_cadastro = 0
   def __init__(self, nome):
       self.nome = nome
       self.alunos = []
   def info(self):
       for i , nome in enumerate(self.alunos):
           print(f"aluno: {nome}, aluno na posicao: {i+1}")

   def adicionar(self):
       aluno = input("Qual o nome do aluno")
       if aluno in self.alunos:
           print("aluno já existente ")
       else:
           self.alunos.append(aluno)
           print("aluno adicionado com sucesso")
   def remover(self):
       aluno = input("Qual o nome do aluno para remover ")
       if aluno not in self.alunos:
           print("aluno não existente ")
       else:
           self.alunos.remove(aluno)
           print("aluno removido com sucesso")

p1 = Produto("ADM")

p1.adicionar()
p1.adicionar()
p1.adicionar()
p1.adicionar()
p1.remover()
p1.info()