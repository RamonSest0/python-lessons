"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y=None, z=None): # se enviamos um valor padrão todos os outros após tbm terão que ter um valor padrão
    if z is not None:
        print(f'{x=} y={y} {z=}', '|' , f'x + y + z = {x + y + z}')
    else: 
        print(f'{x=} y={y}', '|' , f'x + y = {x + y}')

soma(1, 5)
soma(500, 1)
soma(5, 5, 0)