# Crie um programa que leia um valor em metros e mostre convertido em centímetros e milímetros

m = float(input("Digite um valor em metros: "))
cm = m * 100
mm = m * 1000
print("O valor convertido é {}cm e {}mm" .format(cm, mm))
