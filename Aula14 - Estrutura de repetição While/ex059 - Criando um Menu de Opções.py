'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = 0
while option != 5:
    print('''Suas opções são:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    option = int(input('>>> Escolha sua opção: '))
    if option == 1:
        soma = n1 + n2
        print('A soma é {}.'.format(soma))
    elif option == 2:
        produto = n1 * n2
        print('O produto é {}.'.format(produto))
    elif option == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é {}.'.format(maior))
    elif option == 4:
        print('Insira os novos valores:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif option == 5:
        print('Encerrando o programa...')
    else:
        print('[ERRO] Opção inválida! Tente novamente.')
print('Você encerrou o programa!')
