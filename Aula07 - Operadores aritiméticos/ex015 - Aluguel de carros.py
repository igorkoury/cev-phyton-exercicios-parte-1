# Crie um programa que pergunte a quantidade de Km percorridos por um carro alugada e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00/dia e R$ 0,15/km.

d = int(input("Por quantos dias o carro ficou alugado? "))
km = float(input("Quantos km foram percorridos com o carro? "))
t = (d * 60) + (km * 0.15)
print("O total a pagar pelo aluguel do carro é de R$ {:.2f}" .format(t))
