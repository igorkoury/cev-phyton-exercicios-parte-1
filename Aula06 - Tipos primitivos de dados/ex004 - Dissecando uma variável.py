# Faça um programa que leia algo pelo teclado, mostre na tela o seu tipo primitivo e todas as informações possíveis

n = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(n))
print("É um número?", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())
print("Está minúsculo?", n.islower())
print("Está maiúsculo?", n.isupper())
print("Está capitalizado?", n.istitle())
print("É apenas espaços?", n.isspace())
