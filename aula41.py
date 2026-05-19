"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutáveis)
"""

lista_a = ['Ramon', 'Ana Julia']
lista_b = lista_a

lista_b[0] = 'Qualquer coisa' # alteremos a lista_a, porém como a lista_b aponta promesmo valor, ela vai mostrar a alteração. Diferente de um dado imutável como ex. abaixo

print(lista_b)
print(lista_a)

nome = "Ramon"
nome_b = nome

nome = "Ana Julia"
print(nome, nome_b)

