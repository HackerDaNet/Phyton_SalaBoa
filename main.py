from tokenize import String

idade = 18

altura = 1.75

nome = "João"

aprovado = True

frutas = ["maça", "banana", "uva"]

cores = ("azul", "verde", "vermelho")

aluno = {
    "nome": "Maria",
    "idade": 18,
    "curso": "Desenvolimento de Sistemas"
}

print("Exemplo de Tipos de dados em phyton")

print("idade =", idade)
print("Tipo: ", type(idade))

print("altura =", altura)
print("Tipo: ", type(altura))

print("\nnome = ", nome)
print("Tipo:", type(nome))

print("\naprovado = ", aprovado)
print("Tipo:", type(aprovado))

print("\nfrutas =", frutas)
print("Tipo:", type(frutas))

print("\ncores = ", cores)
print("Tipo:", type(cores))

print("\naluno = ", aluno)
print("Tipo:", type(aluno))

#exemplo 2

print("Digite seu nome:")
nome = input()

print("Digite sua idade:")
idade = int(input())

print("Digite a quantia em dinheiro")
dinheiro = float(input())

print("Nome: ", nome, " ", idade, " ", "R$ ", f"{dinheiro:.2f}")

#print(f"Nome {nome} - {idade} anos - R$ {dinheiro:.2f}")

print("Digite o item que quer cadastrar")
item = str(input())

print("Digite a quantidade do item")
quantidade = int(input())

print("Digite o preço unitario")
preco = float(input())

print("Item: ", item, " Quantidade: ", quantidade, " Preço: ", preco)

#Calculando a idade futura

print("Qual sua idade?")
idade2 = int(input())
print("Sua idade daqui 5 anos será: ", idade2+5)