'''Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias
de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos
 interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.'''

num = soma = cont = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print('Você digitou {} números. '.format(cont), end='')
print(f'A soma entre eles vale {soma}.') # python 3.6
