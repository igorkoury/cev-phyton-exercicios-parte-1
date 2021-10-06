#    Faça um programa que leia 3 números e diga qual é o maior e o menor.

print("Digite 3 numeros para saber quem é o menor e o maior.")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro: "))
n3 = int(input("Digite mais um: "))
print("Você digitou {}, {} e {} respectivamente.".format(n1, n2, n3))
menor = n1
if n1 > n2 and n3 > n2:
    menor = n2
if n2 > n3 and n1 > n3:
    menor = n3
maior = n1
if n1 < n2 and n1 < n3:
    maior = n2
if n2 < n3 and n1 < n3:
    maior = n3
print("O menor valor digitado foi {}.".format(menor))
print("O maior valor digitado foi {}.".format(maior))
