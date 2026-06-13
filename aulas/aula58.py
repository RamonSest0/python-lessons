"""
args = Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma1 = soma(1, 2, 3)
print(soma1)
outra_soma = soma(5, 5, 5)
print(outra_soma)

