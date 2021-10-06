# Operadores aritiméticos

# soma +
# subtração -
# multiplicação *
# divisão /
# potenciação **
# divisão inteira //
# resto da divisão %

# função interna de potência pow(2, 2) = 4
# raiz quadrada 25**(1/2) = 5

n1 = int(input("digite um número: "))
n2 = int(input("Digite outro: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print("A soma é {}, a multiplicação é {}, a divisão é {:.2f}".format(s, m, d),
      end=' ')  # faz os printes sairem na mesma linha
print("A divisão inteira é {}, o resto da divisão é {} e a exponenciação é {}.".format(di, r, e))

# end=" " faz os prints saírem na mesma linha
# \n faz uma quebra de linha nos prints