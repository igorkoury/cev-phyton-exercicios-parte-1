""" Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

print('='*40)
print('{: ^40}'.format('NÚMEROS PRIMOS'))
print('='*40)

total = 0
num = int(input('Digite um número: '))
for numeros in range(1, num+1):
    if num % numeros == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(numeros, end=' ')
print('\n\033[mO número {} foi dividido {} vezes, portanto: '.format(num, total))
if total == 2:
    print('É um número primo.')
else:
    print('Não é um número primo')
