'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('~' * 30)
print('{:^30}'.format('BANCO DO IGOR'))
print('~' * 30)
print('Este caixa opera com as cédulas de 100, 50, 20, 10, 5 e 2 reais.')
valor = int(input('Qual valor você gostaria de sacar? R$ '))
totCed = 0
ced = 100
while True:
    if valor >= ced:
        valor -= ced
        totCed += 1
    else:
        if ced > 0:
            print(f'Você sacou {totCed} cédulas de R${ced}.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totCed = 0
        if valor == 0:
            break
print('Obrigado por utilizar o BANCO DO IGOR.')
