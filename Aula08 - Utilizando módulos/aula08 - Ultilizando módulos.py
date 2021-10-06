# Utilizando módulos

# import - importa um bibliotéca
# from "math" import "trunc" - importa uma função específica de dentro de uma bibliotéca

# Principais funções da bibliotéca "math":
# ceil - faz o arredondamento do valor para cima
# floor - faz o arredondamento do valor para baixo
# trunc - torna o número inteiro, eliminando as casa depois da vírgula sem fazer arredondamento nenhum
# pow - potência
# sqrt - raíz quadrada
# factorial - calcula o fatorial de um número


# Exemplos:

# Forneça a raíz quadrada de um número qualquer:
# import math
# n = int(input("Digite um número: "))
# raiz = math.sqrt(n)
# print("A raíz quadrada de {} é {:.2f}" .format(n, raiz))

# Forneça a raíz quadrada de um número qualquer, e fça o arredondamento do valor para baixo:
# from math import sqrt, floor
# n = int(input("Digite um número: "))
# raiz = sqrt(n)
# print("A raíz quadrada de {} é {:.2f}" .format(n, floor(raiz)))

# Faça o sorteio de um número inteiro entre 1 e 10:
# import random
# n = random.randint(1, 10)
# print(n)


# De onde importar módulos: https://pypi.org/
