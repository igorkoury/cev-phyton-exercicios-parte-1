''' Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

num = int(input('Quer ver a tabuada de qual valor? '))
while True:
    if num < 0:
        break
    for tab in range(1, 11):
        print(f'{tab:2} x {num:2} = {num * tab}')
    num = int(input('Digite outro número para ver sua tabuada: '))
print('FIM')
