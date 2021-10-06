'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
 normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format('LOJAS KOURY'))
preço = float(input('Informe o valor do produto deseja: R$ '))
print('{:=^40}'.format('Condições de pagamento:'))
print('''Digite [1] à vista dinheiro/cheque: 10% de desconto.
Digite [2] à vista no cartão: 5% de desconto. 
Digite [3] em até x2 no cartão: preço normal.
Digite [4] 3x ou mais no cartão: 20% de juros.''')
cond = int(input('Selecione a condição de pagamento desejada: '))
if cond == 1:
    print('Você escolheu pagar à vista dinheiro/cheque: 10% de desconto.')
    print('O valor final do produto será R$ {:.2f}.'.format(preço * 0.9))
elif cond == 2:
    print('Você escolheu pagar à vista no cartão: 5% de desconto.')
    print('O valor final do produto será R$ {:.2f}.'.format(preço * 0.95))
elif cond == 3:
    print('Você escolheu pagar em até x2 no cartão: preço normal.')
    print('O valor final do produto será x2 R$ {:.2f}.'.format(preço / 2))
elif cond == 4:
    print('Você escolheu pagar em 3x ou mais no cartão: 20% de juros')
    print('O valor final do produto será R$ {:.2f}.'.format(preço * 1.2))
