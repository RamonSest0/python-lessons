name = input('Qual é o seu primeiro nome? ')

len_name = len(name)

if len_name > 1:
    if len_name <= 4:
        print('Seu nome é muito pequeno.')
    elif len_name <= 5:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')

else:
    print('Digite mais de uma letra.')