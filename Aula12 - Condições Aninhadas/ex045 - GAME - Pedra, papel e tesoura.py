'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)

print('{:=^50}'.format(' BEM VINDO AO GAME '))
print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jog = int(input('Qual sua escolha? '))

from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 10)
print('O computador escolheu {}'.format(itens[comp]))
print('O jogador escolheu {}.'.format(itens[jog]))
print('-=' * 10)

if comp == 0:
    if jog == 0:
        print('EMPATE')
    if jog == 1:
        print('JOGADOR VENCEU')
    if jog == 2:
        print('COMPUTADOR VENCEU')
elif comp == 1:
    if jog == 0:
        print('COMPUTADOR VENCEU')
    if jog == 1:
        print('EMPATE')
    if jog == 2:
        print('JOGADOR VENCEU')
elif comp == 2:
    if jog == 0:
        print('JOGADOR VENCEU')
    if jog == 1:
        print('COMPUTADOR VENCEU')
    if jog == 2:
        print('EMPATE')
