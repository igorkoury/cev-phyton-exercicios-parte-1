# Estrutura condicional aninhada:
#
# if carro.esquerda():
#     bloco 01
# elif carro.esquerda:
#     bloco 02
# elif carro.ré:
#     bloco 03
# else:
#     bloca 04

nome = str(input("Qual é o seu nome? ")).strip()
if nome == "Igor":
    print("Que belo nome você tem!")
elif nome == 'Pedro' or nome == 'João' or nome == 'Gustavo':
    print('Seu nome é bem comum aqui no Brasil...')
elif nome in 'Leilane Duda Maria Eduarda':  
    print('Mas que belo nome feminino!')
else:
    print('Seu nome é um nome legal...')
print("Tenha um bom dia, {}!".format(nome))

