'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = maisDeMil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    # a) total gasto
    total += preco
    # b) conta quantos produtos custam mais de mil
    if preco > 1000:
        maisDeMil += 1
    # c) identificando o produto mais barato
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':  # validando a continuação
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM')
print(f'O total gasto na compra foi de R${total:.2f}.')
print(f'No total, {maisDeMil} produtos custaram mais de R$ 1000,00.')
print(f'O produto mais barato foi {barato.upper()} que custa R${menor:.2f}.')
