"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista_compras = []
novo_item = ''

while True:
    do_it = input('Selecione uma opção [i]nserir, [a]pagar, [l]istar: ')

    if do_it.lower() == 'i':
        novo_item = input('Digite o item que você quer incluir na lista de compras: ')
        if novo_item == '':
            print('Você não digitou nada. Tente novamente.')
            continue
        lista_compras.append(novo_item)
        for i, item in enumerate(lista_compras, start=1):
            print(f'{i} - {item}')
        print('Item adicionado com sucesso a lista de compras.')

    if do_it.lower() == 'a':
        if lista_compras == []:
            print('Não há itens na lista para serem apagados')
            continue

        for i, item in enumerate(lista_compras, start=1):
            print(f'{i} - {item}')
        apagar_item = input('Qual item você quer remover da lista (digite o número): ')

        try:
            del lista_compras[int(apagar_item) - 1] # - 1 para ajustar o valor para o index correto
        except:
            print('O item não existe na lista ou digito inválido. Tente novamente.')
            continue

    if do_it.lower() == 'l':
        for i, item in enumerate(lista_compras, start=1):
            print(f'{i} - {item}')
    
    else:
        print('Digito inválido. Tente novamente.')
        continue
    
    saida = input('Deseja sair? [s]im ou n[ão]')

    if saida.lower() == 's':
        break
    elif saida.lower() == 'n':
        continue
    else:
        print('algo deu errado :(')
        continue

    