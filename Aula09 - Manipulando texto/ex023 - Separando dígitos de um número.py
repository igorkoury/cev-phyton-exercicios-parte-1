# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos desse número separados em linhas

n = int(input("Digite um número de 0 a 9999: ").strip())
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("Analisaando o número {}:".format(n))
print("Unidade {}".format(u))
print("Dezena {}".format(d))
print("Centena {}".format(c))
print("Milhar {}".format(m))




#num = int(input("Digite um número de 0 a 9999: "))
#u = num // 1 % 10
#d = num // 10 % 10
#m = num // 1000 % 10
#print("Analisando {}, temos:".format(num))
#print("Unidaade: {}".format(u))
#print("Dezena {}".format(d))
#print("Centena: {}".format(c))
#print(("Milhar: {}".format(m)))
