# requisições ao usuário = nome e idade

name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

if name == '' or age == '':
    print('Desculpe você deixou campos vazios. :(')
else:
    print(f'Seu nome é: {name}')
    print(f'Seu nome invertido é: {name[::-1]}')
    
    if ' ' in name:
        print('Seu nome contém espaços.')
        print(f'Seu nome contém {(len(name) - 1)} letras.')
        
    else:
        print('Seu nome não contém espaços.')
        print(f'Seu nome contém {len(name)} letras.')

    print(f'A primeira letra do seu nome é: {name[0]}')
    print(f'A última letra do seu nome é: {name[-1]}')

    