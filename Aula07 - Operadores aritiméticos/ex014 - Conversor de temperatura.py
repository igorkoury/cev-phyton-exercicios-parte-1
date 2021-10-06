# Crie um programa que receba a temperatura em Celsius e converta essa temperatura para Kelvin e Fahrenheit:

c = float(input("Digite a temperatura em Celsius: "))
f = c * (9/5) + 32
k = c + 273.15
print("{} ºF\n{} K" .format(f, k))
