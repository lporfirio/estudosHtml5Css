'''
ANSI escape sequence

\033[style;text;back m

style
0 - normal
1 - bold
4 - sublinhado
7 - negative

text
30 - white
31 - red
32 - green
33 - yellow
34 - blue
35 - purple
36 - light blue
37 - gray

back
40 - white
41 - red
42 - green
43 - yellow
44 - blue
45 - purple
46 - light blue
47 - gray

'''

print('\033[0;31mvermelho\033[m')

a = 1
b = 4
print('os valores são \033[32m{}\033[m e \033[36m{}\033[m!!!'.format(a, b))
