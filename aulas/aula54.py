"""
Argumentos nomeados e não noemados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|' , f'x + y + z = {x + y + z}')

soma(1, 5, 9)
soma(y=7, x=5, z=9)