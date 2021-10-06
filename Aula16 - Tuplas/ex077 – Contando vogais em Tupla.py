'''Exercício Python 077: Crie um programa que tenha uma tupla com várias
palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.'''

palavras = ('Igor', 'Rosi', 'Tavares',
         'Leilane', 'Maria', 'Eduarda')

for p in palavras:
    print(f'\nNa plalavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
