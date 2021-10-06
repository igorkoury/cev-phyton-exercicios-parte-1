#   Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
#   superiores a R$ 1.250,00 calcule um aumento de 10% e para inferiores, ou iguais, um aumento de 15%.

sal = float(input("Digite seu salário: R$ "))
aum1 = sal * 1.10
aum2 = sal * 1.15
if sal > 1250:
    print("Com aumento de 10% seu novo salário é {:.2f}.".format(aum1))
else:
    print("Com aumento de 15% seu novo salário é {:.2f}.".format(aum2))
