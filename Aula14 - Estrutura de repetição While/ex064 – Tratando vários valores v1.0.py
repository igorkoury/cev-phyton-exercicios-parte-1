'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont = cont + 1
    soma = soma + num
print('PROGRAMA FINALIZADO')
cont = cont - 1
print('Você digitou {} números.'.format(cont))
soma = soma - 999
print('A soma entre eles é {}.'.format(soma))
