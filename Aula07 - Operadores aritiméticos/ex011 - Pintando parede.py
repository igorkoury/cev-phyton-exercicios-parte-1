# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pinta-la. Sabendo que cada litro de tinta pinta uma área de 2m²

x = float(input("Digite a largura da parede: "))
y = float(input("Digite a altura da parede: "))
a = x * y
tinta = a / 2
print("A área da parede corresponde a {:.2f} m²." .format(a), end=" ")
print("A qauntidade de tinta necessária para pinta-la é de {:.2f} litros." .format(tinta))
