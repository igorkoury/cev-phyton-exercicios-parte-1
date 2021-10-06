'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior18 = homem = mulherMenor20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':   # validando a resposta 'sexo'
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:   # quantas pessoas tem mais de 18 anos
        maior18 += 1
    if sexo == 'M':   # quantos homens foram cadastrados
        homem += 1
    if sexo == 'F' and idade < 20:   # quantas mulheres tem menos de 20 anos
        mulherMenor20 += 1
    resposta = ' '
    while resposta not in 'SN':   # validando a continuação
        resposta = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{maior18} pessoas com mais de 18 anos foram cadastradas.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulherMenor20} mulheres com menos de 20 anos foram cadastradas.')
print('FIM')
