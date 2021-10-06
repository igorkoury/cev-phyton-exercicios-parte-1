'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

ano = int(input('Digite seu ano de nascimento: '))
from datetime import date
anoatual = date.today().year
idade = anoatual - ano
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM: atletas até 9 anos.')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL: atletas até 14 anos.')
elif idade > 14 and idade <= 19:
    print('Categoria JÚNIOR: atletas até 19 anos.')
elif idade > 19 and idade <= 25:
    print('Categoria SÊNIOR: atletas até 25 anos.')
elif idade > 25:
    print('Categoria MASTER: atleta até 25.')
