
import random
#Exercisio 4

print("Digite seu dinheiro")
dinheiro = float(input())

dolar = dinheiro * 5.08

print(dolar)

#Exercisio 5

print("Qual a altura")
altura = float(input())

print("Qual a base")
base = float(input())

area = (base * altura)/2

print(area)

#Exercisio 6

print("Qual a 1 nota do aluno")
nota1 = float(input())
print("Qual a 2 nota do aluno")
nota2 = float(input())
print("Qual a 3 nota do aluno")
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

print(media)

#Exercisio 7

print("Qual seu nome")
nome = str(input())

print("Qual a idade")
idade = int(input())

print("Qual a cidade")
cidade = str(input())

print("Qual o curso")
curso = str(input())

print("Meu nome é", nome," Tenho: ", idade, " Anos e moro em ", cidade," faco o curso de: ", curso)

#Exercisio 8

print("Digite o numero que queira a tabuada")
numero = int(input())

for i in range(1, 11):
    print(numero*i)

#Exercisio 9
v = 0
v2 = 0
v3 = 0
v4 = 0

print("Qual a quantidade de votos que devera ter")
i7 = int(input())
for v in range(i7):
    print("Digite seu voto, 1 - João. 2 - Ana. 3 - Pedro.")
    v = int(input())
    if v == 1:
        v2 = v2 + v
    if v == 2:
       v3 = v3 + v
    if v == 3:
        v4 = v4 + v

if(v2 > v3 and v2 > v4):
    print("O ganhador foi o João")
if(v3 > v2 and v3 > v4):
    print("O ganhador foi a Ana")
if(v4 > v3 and v4 > v2):
    print("O ganhador foi a Pedro")

#Exercisio 10
print("Me diga seu nickname de login")
nome = str(input())
print("Qual sua senha de login")
senha = str(input())

tentativas = 5

sucessoLogin = False

while(sucessoLogin == False):
    print("Digite seu login")
    login = str(input())
    print("Digite sua senha")
    senha1 = str(input())
    if(login == nome and senha == senha1):
        print("Login foi bem sucedido")
        sucessoLogin = True
        break
    else: print("Tentativa inválida, tente novamente, tentativas restantes: ", tentativas)
    sucessoLogin = False
    tentativas = tentativas - 1
    if (tentativas == 0):
        print("Você foi bloqueado, tentativas esgotadas")
        quit()

#Exercisio 11

import random
# Sorteia um número entre 1 e 100
numeroR = random.randint(1, 100)
c = 1
for c in range(5):
    print("Qual seu palpite?")
    palpite = int(input())
    if(numeroR == palpite):
        print("Você acertou!")
    if(numeroR > palpite):
        print("O numero é maior que sue palpite")
    if(numeroR < palpite):
        print("O numero é menor que seu palpite")
    c = c + 1
if(c == 5):
    print("O numero era: ", numeroR)

#Exercisio 12
j = 0
for j in range(5):
  print("*" * j)
#Exercisio 13
print("Qual o numero")
numero11 = int(input())
somador = 0
for i12 in range (1, numero11+1):
    if(numero11 % i12 == 0):
        somador = somador + 1

if(somador > 2):
    print("Não é primo")
else:
    print("Primo")
