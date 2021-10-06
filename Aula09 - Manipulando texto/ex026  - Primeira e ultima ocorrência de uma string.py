# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. quantas vezes aparece a letra "a"
# 2. em que posição aparece a primeira vez
# 3. em que posição ela aparece a ultima vez

frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra 'a' aparece {} vezes na frase".format(frase.count("a")))
print("A primeira  posição é a {}".format(frase.find("a")+1))
print("A ultima a posição é a {}".format(frase.rfind("a")+1))
