# Crie um programa que leia um valor em real e mostre-o convertido em dolar, euro e yen

r = float(input("Digite um valor em reais: "))
d = 5.06
e = 6.16
y = 0.046
print("U$ {:.2f} \n€ {:.2f} \n¥ {:.2f}" .format(r/d, r/e, e/y))
