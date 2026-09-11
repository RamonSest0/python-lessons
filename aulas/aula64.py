p1 = {
    'nome': 'Ramon',
    'sobrenome': 'Sesto',
}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update(nome='Opa', idade=26)
# print(p1)

tupla = (('nome', 'novo nome'), ('idade', 26))
lista = [['nome', 'novo nome'], ['idade', 26]]
p1.update(lista)
print(p1)