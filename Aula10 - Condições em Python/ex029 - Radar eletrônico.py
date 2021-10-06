# Escreva um programa que leia a velociadade de um automóvel. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

v = int(input("Qual velocidade do automóvel? "))
m = (v - 80) * 7
if v > 80:
    print("Você ultrapassou a velocidaade permitida de 80 km/h!")
    print("Você foi multado em R$ {}.".format(m))
else:
    print("Muito bem! Continue respeitando os limites de velocidaade.")
