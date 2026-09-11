# Exemplo de uso de sets

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if 'r' in letras:
        print('A letra "r" foi achada.')
        break

    print(letras)