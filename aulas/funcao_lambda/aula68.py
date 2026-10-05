a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': "Ramon",
    'sobrenome': 'Sesto',

}

a, b = pessoa
print(a, b)
a, b = pessoa.values()
print(a, b)
a, b = pessoa.items()
print(a, b)

# desempacotando

(a1, a2), b = pessoa.items()
print(a1, a2)

for chave, valor in pessoa.items():
    print('chave', chave)
    print('valor', valor)


pessoa2 = {
    'nome': "Ana Julia",
    'sobrenome': 'Barbosa',

}

dados_pessoa = {
    'idade': 22,
    'altura': 1.6,
}

pessoa_completa = {**pessoa2, **dados_pessoa}
print(pessoa_completa)

def mostro_argumentos_nomeados(**kwargs):
    print(kwargs)


mostro_argumentos_nomeados(nome='Ramon', idade=26, altura=1.6)