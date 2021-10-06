# Agora o professor deseja sortear a ordem de apresentação dos seus alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a1 = str(input("Aluno 1: "))
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A sequência de apresentação será:")
print(lista)
