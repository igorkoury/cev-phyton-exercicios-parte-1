#   Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem considerando:
#   R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas.

dis = int(input("Informe a distância da viagem em km? "))
ate200 = dis * 0.50
maior = dis * 0.45
if dis <= 200:
    print("Considerando a distância da viagem (menor que 200 km) o valor cobrado será R$ {:.2f}".format(ate200))
else:
    print("Considerando a distância da viagem (maior que 200 km) o valor cobrado será R$ {:.2f}".format(maior))


