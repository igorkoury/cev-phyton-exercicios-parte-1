'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
from time import sleep
print('Analisando os números escolhidos...')
sleep(1)
print('Você escolheu os números \033[33m{}\033[m e \033[33m{}\033[m.'.format(n1, n2))
if n1 > n2:
    print('O \033[33mprimeiro\033[m valor é maior.')
elif n1 < n2:
    print('O \033[33msegundo\033[m valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, os números \033[33msão iguais\033[m.')
# else:
#     print('Um ou mais números \033[31mnão são inteiros/033[m foram detectados. Tente novamente escolhendo valores \033[32minteiros\033[m.')
