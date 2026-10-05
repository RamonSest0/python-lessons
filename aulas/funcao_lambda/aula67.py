def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(
        lambda x, y: x + y, 2, 3
    ), 
    executa(soma, 2, 3)
)

duplica = cria_multiplicador(2)
triplica = cria_multiplicador(3)
quadriplica = cria_multiplicador(4)

print(duplica(5))
print(triplica(2))
print(quadriplica(3))