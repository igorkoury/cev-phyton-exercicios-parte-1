# Faça um programa que leia o nome completo de uma pessoa e em siguida mostre o primeiro e o ultimo separadamente

nome = ("Igor José Koury Tavares").strip()
n = nome.split()
print("Primeiro nome: {}".format(n[0]))
print("Ultimo nome: {}".format(n[-1]))
