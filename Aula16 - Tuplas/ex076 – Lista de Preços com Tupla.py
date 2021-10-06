'''Exercício Python 076: Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ('Lapis', 1.75,
            'Caneta', 2.50,
            'Borracha', 1.5,
            'Corretivo', 2.75,
            'Apontador', 2.00)

print('~'*40)
print(f'{"LISTA DE MATERIAIS":^40}')
print('~'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:.2f}')
print('~'*40)
