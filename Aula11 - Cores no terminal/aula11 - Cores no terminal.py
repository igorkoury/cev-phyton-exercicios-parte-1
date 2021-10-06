"""Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus
programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

Formato do padrão ANSI:

\033[0;33;44m

onde:
0: style
33: text
44: back

style:              text:               back:
0 - none            30 - white          40 - white
1 - bold            31 - red            41 - red
4 - underline       32 - green          42 - green
7 - negative        33 - yellow         43 - yellow
                    34 - blue           44 - blue
                    35 - purple         45 - purple
                    36 - cyan           46 - cyan
                    37 - gray           47 - gray"""

print("\033[1;31;43mOlá, mundo!\033[m")
print("\033[0;30;41mOlá, mundo!\033[m")
