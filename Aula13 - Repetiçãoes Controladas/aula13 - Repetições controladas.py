''' Estrutura de repetição (for)

Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e
simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)


for C in range(0,10):   # para um comando
    passo
pegar

for C in range(0,3):    # para dois comandos
    passo
    pula
passo
pegar

for C in range(0,3):    # para dois comandos
    if moeda:
        pegar
    passo
    pula
passo
pegar
'''

for c in range(0, 6):   # repete "oi" x5
    print('oi')
print('Fim')

for c in range(0, 6):   # conta de 0 até 5
    print(c)
print('Fim')

for c in range(0, 6, 2):   # conta de 0 até 5, pulando de 2 em 2
    print(c)
print('Fim')

for c in range(5, -1, -1):   # conta de 5 até 0
    print(c)
print('Fim')
