"""
enumerate - enumera iteráveis (índices)

Ele permite percorrer uma estrutura:

pegando o VALOR
E a POSIÇÃO ao mesmo tempo
"""

nomes = ['Ramon', 'Ana Julia', ':)']

for i, nome in enumerate(nomes):
    print(f'{i} - {nome}')

frutas = ['banana', 'maça', 'goiaba']

for i, fruta in enumerate(frutas, start=1):
    print(i, fruta)