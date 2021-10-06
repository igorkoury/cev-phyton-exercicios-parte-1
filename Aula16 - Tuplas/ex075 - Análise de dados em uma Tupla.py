'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite um ultimo número: ')))

print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O número 3 não foi digitado nenhuma vez')
else:
    print(f'O númeor 3 foi digitado na posição {num.index(3)+1}')
print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')
