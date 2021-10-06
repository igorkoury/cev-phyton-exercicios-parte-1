'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

print('='*40)
print('{: ^40}'.format('AVALIAÇÃO DE IDADE'))
print('='*40)
totalmaior = 0
totalmenor = 0
from datetime import date
for pess in range(1, 8):
   nasc = int(input('Em que ano nasceu a {}º pessoa? '.format(pess)))
   anoatual = date.today().year
   idade = anoatual - nasc
   if idade >= 18:
      totalmaior += 1
   else:
      totalmenor += 1
print('\033[32m{}\033[m pessoas atingiram a maior idade e \033[31m{}\033[m pessoas ainda não atigiram.'.format(totalmaior, totalmenor))
