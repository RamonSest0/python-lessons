"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

O if não impede que erros (exeções) aconteçam
"""

numero_str = input('Digite um número para ser dobrado: ')

try: # tenta executar o código
    soma_float = float(numero_str) * 2
    print(f'O dobro de {numero_str} é {soma_float:.2f}')
except: # e ocorrer algum erro dentro do try, execute:
    print('Você não digitou um número.')

# if numero_str.isdigit():
#     soma_float = float(numero_str) * 2
#     print(f'O dobro de {numero_str} é {soma_float:.2f}')
# else:
#     print('Você não digitou um número.')

