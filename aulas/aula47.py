"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Frase qualquer, bla, bla, bla'
lista_palavras_initial = frase.split(',')
lista_palavras_fixed = []


for i, frase in enumerate(lista_palavras_initial):

    lista_palavras_fixed.append(lista_palavras_initial[i].strip()) # strip() remove os espaços (lstrip() e rstrip() corta apenas espaços da esquerda ou direita (Left and Right))

print(lista_palavras_fixed)

frases_unidas = '.'.join(['aaa', 'bbb', 'ccc', 'ddd']) # dentro de '' antes do método join() passamos o separador
lista_unida = ', '.join(lista_palavras_fixed)
print(frases_unidas)
print(lista_unida)