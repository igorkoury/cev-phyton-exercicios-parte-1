'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

print('Para calcular seu IMC digite preencha os campos abaixo:')
altura = float(input('Qual a sua altura em metros (m)? '))
peso = float(input('Qual seu peso em quilos (kg)? '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc <= 18.4:
    print('Seu IMC está abaixo de 18,5: Você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC está entre 18,5 e 25: Você está no seu PESO IDEAL.')
elif imc >= 25.1 and imc <= 30:
    print('Seu IMC está entre 25 e 30: Você está com SOBREPESO.')
elif imc >= 30.1 and imc <= 40:
    print('Seu IMC está entre 30 e 40: Você está com OBESIDADE.')
elif imc > 40:
    print('Seu IMC está acima de 40: Você está com OBESIDADE MORBIDA.')
