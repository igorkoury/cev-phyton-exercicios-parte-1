'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('~' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')  # a) Os 5 primeiros times.
print('~' * 15)
print(f'O 4 ultimos colocados são {times[-4:]}')  # b) Os últimos 4 colocados.
print('~' * 15)
print(f'O times em ordem alfabética: {sorted(times)}')  # c) Times em ordem alfabética.
print('~' * 15)
chape = times.index('Chapecoense') + 1  # d) Em que posição está o time da Chapecoense.'''
print(f'O time da Chapecoense aparece na {chape}ª posição')
print('~' * 15)