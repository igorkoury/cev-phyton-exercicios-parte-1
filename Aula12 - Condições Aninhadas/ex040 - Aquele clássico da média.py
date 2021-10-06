'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a nota da primeira avaliação: '))
nota2 = float(input('Digite a nota da segunda avaliação: '))
media = (nota1+nota2) / 2
print('Sua média foi {}.'.format(media))
if 0 >= media < 5:
    print('Média abaixo de 5, você foi REPROVADO.')
elif media >= 5 and media <= 6.9:
    print('Média entre 5.0 e 6.9. Você está de RECUPERAÇÃO.')
elif media >= 7 and media <= 10:
    print('Média superior a 7. Parabéns, você foi APROVADO!')
else:
    print('O valor digitado não é válido. Por favor, tente novamente digitando valores válidos.')
