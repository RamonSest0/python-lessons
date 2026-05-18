"""

Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue eu iterador

"""

texto = 'Ramon'
iterador = iter(texto)

while True: 
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break