'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

resp = cont = soma = maior = menor = 0
while resp != 'N':
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
print('FIM DO PROGRAMA')
print('RESULTADO...')
media = soma / cont
print('Você digitou {} números média dos números digitados é {}.'.format(cont, media))
print('O menor número que você digitou foi {} e o maior foi {}.'.format(menor, maior))
