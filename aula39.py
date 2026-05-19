"""
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido (tbm retorna o item removido)
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40, 50]
lista.append(60)
nome = lista.pop()
del lista[-1] # [-1] sempre será o último item, assim como [0] o primeiro
print(lista, f'O item removido pelo pop() foi: {nome}')

lista.clear()
print(lista)

lista.insert(0, 10)
lista.insert(1, 20)
lista.insert(0, 30)
print(lista)