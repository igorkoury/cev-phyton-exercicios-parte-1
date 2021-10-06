#   Crie um programa que leia um número inteiro na tela e diga se ele é par ou ímpar

num = int(input("Digite um número qualquer: "))
res = num % 2
if res == 0:
    print("O número escolhido é PAR.")
else:
    print("O númeor escolhido é ÍMPAR.")
