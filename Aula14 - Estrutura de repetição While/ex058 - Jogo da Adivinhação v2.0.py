'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.'''

from random import randint
computador = randint(0, 10)
print(computador)

palpite = 1
acertou = False
while not acertou:
    jogador = int(input('Dê seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... Tente outra vez!')
        elif jogador > computador:
            print('MENOS... Tente outra vez!')
print('PARABÉNS! Você acertou em {} palpites.'.format(palpite))
