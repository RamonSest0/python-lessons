"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber  valores oar parâmetros (argumentos)
e retornar valores específicos
Por padrão, funções Python retornam None (nada)
"""

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    if nome.lower() == 'ana julia':
        print(f'Olá, amor da minha vida!')
    else:
        print(f'Olá, {nome}!')

saudacao('Ramon')
saudacao('Ana Julia')
saudacao()
