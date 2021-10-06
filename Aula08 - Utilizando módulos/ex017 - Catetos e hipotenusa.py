# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e mostri o comprimento da sua hipotenusa

# co = float(input("Informe o comprimento do cateto oposto: "))
# ca = float(input("Irforme o comprimento do cateto adjacente: "))
# hi = ((co ** 2) + (ca ** 2)) ** (1/2)
# print("O comprimento da hipotenusa deste triângulo mede {:.2f}" .format(hi))

from math import hypot
co = float(input("Informe o comprimento do cateto oposto: "))
ca = float(input("Irforme o comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("Ocomprimento da hipotenusa deste trinângulo mede {:.2f}".format(hi))
