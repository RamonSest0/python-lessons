"""
Introdução ao desempacotamento + tuples
_ <- variavel que não vai ser usada (convenção Python)
* <- dito de modo simples usamos para que o "resto" da lista fique na variável (*variavel)
"""

nome1, nome2, nome3, nome4 = ['Ramon', 'Ana Julia', 'Luiz', ':)'] # o número de varias e valores precisam ser o mesmo, se não gera um erro
print(nome2)

_, ingrediente, *outros_ingredientes = ['arroz', 'batata', 'feijão', 'carne', 'tomate']
print(ingrediente)
print(outros_ingredientes) # retorna o resto da list
