# Manipulando chaves e valores em dicíonarios

pessoa = {}

chave = input('Oi! Digite sua chave:')
valor = input('Digite o valor dessa chave:')

pessoa[chave] = valor
pessoa['sobrenome'] = 'Sesto'

del pessoa['sobrenome']

print(pessoa)