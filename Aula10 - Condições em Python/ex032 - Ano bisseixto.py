#    Faça um programa que leia um ano qualquer e mostre se ele é bisseixto

from datetime import date
ano = int(input("Qual ano você gostaria de analisar? \nSe quiser analisar o ano atual digite 0: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} É um ano bisseixto.".format(ano))
else:
    print("O ano {} NÃO É um ano bissexto.".format(ano))
