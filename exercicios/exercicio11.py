# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def operacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = operacao(2)
triplicar = operacao(3)
quadruplicar = operacao(4)

print(duplicar(2))
print(triplicar(4))
print(quadruplicar(5))