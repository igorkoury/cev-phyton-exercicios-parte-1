# Crie um algorítimo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada

n = float(input("Digite um número: "))
do = n * 2
tr = n * 3
r = n ** (1 / 2)
print("O dobro é {}, o triplo é {} e a raíz quadrada é {}.".format(do, tr, r))