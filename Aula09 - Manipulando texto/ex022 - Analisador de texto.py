# Crie um programa que que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas
# 2. O nome com todas as letras minúsculas
# 3. Quantas letras ao todo sem considerar os espaços
# 4. Quantas letras tem o primeiro nome


nome = "Igor José Koury Tavares".strip()
print("Analisando seu nome...")
print("Letras maiúsculas: {}".format(nome.upper()))
print("Letras minúsculaas: {}".format(nome.lower()))
print("O número de letras no seu nome é: {}".format(len(nome) - nome.count(" ")))
n = nome.split()
print("O seu primeiro nome tem {} letras".format(len(n[0])))
