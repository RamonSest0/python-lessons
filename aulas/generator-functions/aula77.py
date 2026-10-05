# Introdução ás Generator functions em Python
# generator = (n for n in range()) <- estrutura similar a comprehension, porém com ().

def generator1(n=0):
    yield 1 # pausar
    return 'Acabou' # nesse contexto levanta uma exceção de stop interation

def generator2(n=0):
    yield 1
    print('em cima do yield 2')
    yield 2
    print('em cima yield 3')
    print('em cima yield 3')
    yield 3
    print('vou terminar...')
    return 'acabou'

def generator(n=0, maximum=10):
    while True:
        yield n # pausou
        # no next vai executar daqui pra baixo e parar n yild novamente com n atualizado com o numero incrementado
        n += 1

        if n > maximum:
            return 'acabou'
        
gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
