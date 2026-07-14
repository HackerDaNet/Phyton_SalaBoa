#Exercisio 1

print("Qual sua idade?")
idade2 = int(input())
print("Sua idade daqui 5 anos será: ", idade2+5)

#Exercisio 2

print("Que tipo de conta você quer fazer? 1 = + 2 = - 3 = / 4 = *")
calculadora = int(input())
print("Digite o numero 1")
numero1 = int(input())
print("Digite o numero 2")
numero2 = int(input())

if calculadora == 1:
    calculadora = numero1 + numero2
if calculadora == 2:
    calculadora = numero1 - numero2
if calculadora == 3:
    calculadora = numero1 * numero2
if calculadora == 4:
    calculadora = numero1 / numero2

print(calculadora)

#Exercisio 3

print("Digite a temperatura em celsius")
temperatura = int(input())
temperaturaFahrenheit = temperatura * 9 / 5 + 32
print(temperaturaFahrenheit)