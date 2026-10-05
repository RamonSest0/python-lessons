# Introdução ás Generator functions em Python
# generator = (n for n in range()) <- estrutura similar a comprehension, porém com ().

def generator(n=0):
    yield 1 # pausar
    return 'Acabou' # nesse contexto levanta uma exceção de stop interation

gen = generator(n=0)
print(next(gen))
print(next(gen))