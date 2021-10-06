# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu Sen, Cos, e Tang

import math
ang = float(input("Digite um ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print("O ângulo {} tem:\nSen {:.2f}\nCos {:.2f}\nTag {:.2f}".format(ang, sen, cos, tg))
