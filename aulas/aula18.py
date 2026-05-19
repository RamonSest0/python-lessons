primeiro_valor = input('Digite um valor para comparação:')
segundo_valor = input('digite outro valor para comparação:')

if primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual a {segundo_valor=}.')
elif primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}.')
else:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}.')