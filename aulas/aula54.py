"""
Argumentos nomeados e não noemados em funções Python

Argumentos nomeados tem nome com sinal de igual
Argumentos nomeados recebem o nome do parâmetro antes do valor.

Argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.
Argumento não nomeado recebe apenas o argumento (valor)

"""

def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|' , f'x + y + z = {x + y + z}')

soma(1, 5, 9) # não nomeados ou posicionais - 
soma(7, y=5, z=9) # nomeados - se passamos um, todos a seguir tbm precisam ser nomeados, como o exem.