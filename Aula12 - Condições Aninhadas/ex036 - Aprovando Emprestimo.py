'''Escreva um programa para aprovar um empréstimo para comprar uma casa. O programa vai perguntar O VALOR DA CASA,
o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode
exceder 30% do salário, ou então o empréstimo será negado.'''

print('Responda o questioário a seguir para validar o seu empréstimo:')
casa = float(input('Qual valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar o empréstimo? '))
prestmax = (salario * 0.3)
prest = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos, com o seu salário,'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f} .'.format(prest))
if prest > prestmax:
    print('O valor da prestação excede 30% do seu salário, seu empréstimo foi negado')
    print('O valor máximo da sua prestação não pode ser maior que R$ {:.2f}'.format(prestmax))
else:
    print('PARABÉNS!! Seu empréstimo foi aprovado!')
print('Obrigado por procurar o nosso banco!')
