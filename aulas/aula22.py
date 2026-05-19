# Operadorees in e not in
# Strings ão iteráveis
#  0 1 2 3 4 (index positivo) 
#  R a m o n
# -5-4-3-2-1 (index negativo)

nome = 'Ramon'

print(nome[4])
print(nome[-5])

print('R' in nome) # podemos verificar se uma letra especifica está em uma string. Ou também verificar se um conjunto de caracteres está na string.
print('mon' in nome) 

print('mon' not in nome)
print('abc' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}.')