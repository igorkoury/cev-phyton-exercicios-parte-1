  Estrutura condicional:

  if carro.esquerda():
      bloco treu
  else:
      bloco false

  tempo = int(input("Quantos anos tem seu carro? "))
  print("Seu carro é novo" if tempo <= 3 else "Seu carro é velho")

  tempo = int(input("Quantos anos tem seu carro? "))
  if tempo <= 3:
      print("Seu carro é novo")
  else:
      print("Seu carro é velho")


  nome = str(input("Qual o seu nome? "))
  if nome == "Igor":
      print("Que nome lindo você tem!")
  print("Bom dia, {}.".format(nome))


  nome = str(input("Qual o seu nome? "))
  if nome == "Igor":
      print("Que nome lindo você tem!")
  else:
      print("Seu nome é tão normal...")
  print("Bom dia, {}.".format(nome))


  n1 = float(input("Digite a primeiraa nota: "))
  n2 = float(input("Digite a segunda nota: "))
  m = (n1 + n2) / 2
  print("Sua média foi {:.1f}".format(m))
  if m >= 6:
      print("Sua nota foi boa!")
  else:
      print("Sua média foi ruim... Estude mais")

  n1 = float(input("Digite a primeiraa nota: "))
  n2 = float(input("Digite a segunda nota: "))
  m = (n1 + n2) / 2
  print("Sua média foi {:.1f}".format(m))
  print("PARABÉNS!!" if m >= 6 else "Estude mais")
