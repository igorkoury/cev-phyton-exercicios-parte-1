''' Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('A soma dos {} valores PARES é de {}.'.format(cont, soma))
