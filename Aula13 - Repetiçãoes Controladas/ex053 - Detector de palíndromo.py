'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).strip().upper()
print(frase)
palavras = frase.split()
juntas = ''.join(palavras)
print(juntas)
invertida = juntas[::-1]
print(invertida)
if juntas == invertida:
    print('A frase que você digitou é um políndromo.')
else:
    print('A frase que você digitou não é um políndromo.')
