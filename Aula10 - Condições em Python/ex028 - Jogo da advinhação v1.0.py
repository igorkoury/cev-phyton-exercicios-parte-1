# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir o número escolhido pelo computador

#   obs: o programa deverá escrever na tela se o usuário venceu ou perdeu


from random import randint
from time import sleep
comp = randint(0, 5)    # faz o computador escolher um número aleatório entre 0 e 5
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5... Tente adivinhar!")
print("-=-" * 20)
jog = int(input("Em qual número eu pensei, jogador? "))  # jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)
if jog == comp:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu! Eu escolhi o número {}.".format(comp))

