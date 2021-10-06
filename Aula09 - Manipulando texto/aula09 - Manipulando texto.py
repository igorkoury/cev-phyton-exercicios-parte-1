frase = "Curso em vídeo Python"

# Fatiamento

print(frase[9])  # mostra o caracter correspondente a posição 9
print(frase[9:21])  # vai da posição 9 até a posição 21
print(frase[9:21:2])  # inicia na posição 9 e vai até a posição 21, pulando de 2 em 2
print(frase[:5])  # incia na posição 0 e vai até a 5
print(frase[15:])  # vai da posição 15 até o final
print(frase[9::3])  # vai da posição 9 até o final pulando de 3 em 3
print(frase[::-1])  # vai de trás pra frente até o início

# Análise

print(len(frase))  # mostra a quatidade de caracteres existentes na string
print(frase.count("o"))  # mostra quantos "o" existem na string
print(frase.count("o", 0, 13))  # mostra quantos "o" existem entre a posição 0 e 13 na string
print(frase.find("deo"))  # busca na string os caracteres escolhidos e em que posição começa
print(frase.find("Android"))  # quando o caracter buscado não existe na string ele responde com o valor -1
print("Curso" in frase)  # Testa se existe ou não aquele valor na string

# Transformação

print(frase.replace("Python", "Android"))  # substitui os valores dentro da string
print(frase.upper())  # transforma todos os caracteres minúsculos em maiúsculos
print(frase.lower())  # transforma todos os caracteres maiúsculos em minúsculos
print(frase.capitalize())  # transforma a primeira letra da string em maiúscula
print(frase.title())  # transforma a primeira letra de cada palavra na dtring em maiúscola

frase1 = "   Aprenda Python  "

print(frase1.strip())  # remove todos os espaços inúteis no início e no final da string
print(frase1.rstrip())  # remove todos os espaços inúteis no início da string
print(frase1.lstrip())  # remove todos os espaços inúteis no final da string

# Divisão

print(frase.split())  # refaz os indices de posições dos caracteres na string iniciando em cada palavra da posição 0 crindo uma nova lista para cada palavra

# Junção

print("-".join(frase))

# Junção sem os espaços

palavras = frase.split()
junto = ''.join(palavras)
print(junto)

# Junção sem os espaços (de trás pra frente)

print(junto[::-1])

print("""Beauty queen of only eighteen, she had some trouble with herself
He was always there to help her, she always belonged to someone else
I drove for miles and miles, and wound up at your door
I've had you so many times, but somehow I want more""")






