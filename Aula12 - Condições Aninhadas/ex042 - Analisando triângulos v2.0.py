'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

Exercício Python 35: Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não
 for mar um triângulo.'''

r1 = int(input('Digite o comprimento da reta 1: '))
r2 = int(input('Digite o comprimento da reta 2: '))
r3 = int(input('Digite o comprimento da reta 3: '))
if r1 > (r2+r3) or r2 > (r1+r3) or r3 > (r1+r2):
    print('As retas {}, {} e {} não podem formar um triângulo.'.format(r1, r2, r3))
elif r1 == r2 == r3:
    print('Os seguimentos de reta podem formar um triângulo EQUILÁTERO: todos os lados são iguais.')
elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
    print('Os seguimentos de reta podem formar um triângulo ISÓCELES: dois lados iguais e um diferente.')
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('Os seguimentos de reta podem formar um triângulo ESCALENO: todos os lados são diferentes')
