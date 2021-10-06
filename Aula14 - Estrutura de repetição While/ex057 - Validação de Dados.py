'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Digite o sexo: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('[ERRO] Sexo inválido. \nTente outra vez: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
