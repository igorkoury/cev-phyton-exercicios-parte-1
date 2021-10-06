'''Exercício Python 72: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro','cinco',
           'seis', 'sete', 'oito', 'nove', 'dez','onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número [0 - 20]: '))
    if num < 0 or num > 20:
        print('INVALIDO! Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {numeros[num]}')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if resposta == 'N':
        break
print('FIM DO PROGRAMA')

