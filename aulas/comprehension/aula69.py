# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

lista = []

for numero in range(10):
    lista.append(numero)


lista = [numero + 1 for numero in range(10)]


print(lista)