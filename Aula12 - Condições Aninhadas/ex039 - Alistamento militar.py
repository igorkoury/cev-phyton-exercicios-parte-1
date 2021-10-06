'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

ano = int(input('Digite seu ano de nascimento: '))
from datetime import date
ref = int(date.today().year)
idade = ref - ano
if idade < 18:
    print('Você ainda ainda vai se alistar no serviço militar. Faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Essa é a hora exata pra você se alistar!')
else:
    print('Já passou o prazo para o seu alistamento. Você devia te se alista à {} anos.'.format(idade-18))
