'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input('Escreva um número inteiro qualquer: '))
print('''Escolha para qual sistema numérico deseja converte-lo, digitando: 
[1] para binário
[2] para octal
[3] para hexdecimal''')
sistema = int(input('Para qual sistema você deseja converter seu número? '))
if sistema == 1:
    print('Você escolheu o sistema \033[33mBinário\033[m. Convertido, agora o valor é {}'.format(bin(num)[2:]))
    print('\033[33mMuito Obrigado por utilizar nosso conversor!\033[m')
elif sistema == 2:
    print('Você escolheu o sistema \033[33mOctal\033[m. Convertido, agora o valor é {}'.format(oct(num)[2:]))
    print('\033[33mMuito Obrigado por utilizar nosso conversor!\033[m')
elif sistema == 3:
    print('Você escolheu o sistema \033[33mHexadecimal\033[m. Convertido, agora o valor é {}'.format(hex(num)[2:]))
    print('\033[33mMuito Obrigado por utilizar nosso conversor!\033[m')
else:
    print('\033[31mOpção inválida!\033[m Tente novamente escolhendo uma das três opções \033[32mválidas.\033[m')
