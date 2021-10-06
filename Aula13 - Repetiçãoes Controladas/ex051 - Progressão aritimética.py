'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
 10 primeiros termos dessa progressão.'''

print('='*40)
print('{: ^40}'.format('PROGRESSÃO ARITIMÉTICA'))
print('{: ^40}'.format('Termos de 10 de uma PA'))
print('='*40)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = (termo + (10 - 1) * razao) + razao   # fórmula matemática para o enésimo número
for c in range(termo, decimo, razao):
    print('{} -> '.format(c), end=' ')
