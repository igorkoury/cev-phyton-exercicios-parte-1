'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
vitoria = 0
while True:
    jog = int(input('Escolha seu valor: '))
    comp = randint(0, 5)
    total = jog + comp
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Você escolhe PAR ou IMPAR? ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {comp}.')
    print(f'O total deu {jog} + {comp} = {total}')
    print('O resultado foi par ' if total % 2 == 0 else 'O resultado foi IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            vitoria = vitoria + 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 != 0:
            vitoria = vitoria + 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar de novo?')
print(f'Você venceu {vitoria} vezes.')
print('GAME OVER!')
