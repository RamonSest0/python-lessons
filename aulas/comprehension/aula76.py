import sys

# Generator expression, Itarables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

lista = [n for n in range(1000)] # a lista está toda na memória
generator = (n for n in range(1000)) # o gebnerator não. Ele está aguardando a gente pedir o próximo valor

# Generator não tem tamanho, índice e etc...É um elemento que criamos apenas para navegar

print(sys.getsizeof(lista)) # tamanho da lista na memoria
print(sys.getsizeof(generator)) # tamanho com generator - o valor não muda mesmo se aumentarmos o tamanho da lista

