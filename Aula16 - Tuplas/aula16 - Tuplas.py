'''Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas
e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[0])  # hamburguer
print(lanche[1])  # suco
print(lanche[-1])  # pudim
print(lanche[-2])  # pizza
print(lanche[:1])  # ('hamburguer',)
print(lanche[:2])  # ('hamburguer', 'suco')
print(lanche[0:2])  # ('hamburguer', 'suco')
print(lanche[0:3])  # ('hamburguer', 'suco', 'pizza')

print(sorted(lanche)) # escreve o resultado na ordem alfabetica
# ['hamburguer', 'pizza', 'pudim', 'suco'] não altera a Tupla, simplesmente transforma em lista e coloca em ordem

for comida in lanche:  # maneira mais simples, quando não precisa da posição
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
# Eu vou comer hamburguer
# Eu vou comer suco
# Eu vou comer pizza
# Eu vou comer pudim
# Comi pra caramba!

# len = length

for comida in range (0, len(lanche)):  # quando precisa da posição
    print(f'Eu vou comer {lanche[comida]}')
print('Comi pra caramba!')
# Eu vou comer hamburguer
# Eu vou comer suco
# Eu vou comer pizza
# Eu vou comer pudim
# Comi pra caramba!

for pos, comida in enumerate(lanche):  # quando precisa da posição
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
# Eu vou comer hamburguer na posição 0
# Eu vou comer suco na posição 1
# Eu vou comer pizza na posição 2
# Eu vou comer pudim na posição 3
# Comi pra caramba!

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)  # (2, 5, 4)
print(b)  # (5, 8, 1, 2)
print(c)  # (2, 5, 4, 5, 8, 1, 2)
print(len(c))  # 7   o comprimento de 'c' é 7
print(c.count(5))  # quantas vezes está aparecendo o número 5 dentro de 'c' 2
print(c.index(8))  # em que posição está o 8 em 'c'? 4
print(c.index(2, 1))  # onde está o 2 a partir da posição do primeiro 2, que está na posição 0

pessoa = ('Igor', 28, 'M', 106)  # podemos ter dados diferentes dentro das Tupla em Python != de Java
print(pessoa)
# ('Igor', 28, 'M', 106)

del(pessoa)  # Tuplas são imutáveis, mas podem ser apagadas por inteiro. Não da pra deletar só um item.
