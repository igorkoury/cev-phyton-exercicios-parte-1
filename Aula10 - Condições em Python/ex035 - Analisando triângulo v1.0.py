# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não for mar um triângulo

print("=-=" * 10)
print("Analisador de trinângulos!")
print("=-=" * 10)
r1 = int(input("Digite o valor da 1ª reta: "))
r2 = int(input("Digite o valor da 2ª reta: "))
r3 = int(input("Digite o valor da 3ª reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Com esses valores É POSSÍVEL formar um triângulo.")
else:
    print("Com esses valores NÃO É POSSÍVEL formar um triângulo.")
