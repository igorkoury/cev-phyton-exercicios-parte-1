'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for.

Exercício 9: Crie um programa que leia um número pelo teclado e mostre a sua tabuada:
'''

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
