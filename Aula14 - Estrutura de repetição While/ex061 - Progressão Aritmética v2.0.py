''' Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
 termos da progressão usando a estrutura while.'''

print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contador += 1
print('FIM')
