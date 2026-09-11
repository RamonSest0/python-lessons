perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': [2, 5, 4, 8],
        'Resposta': 4,
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': [15, 35, 20, 25],
        'Resposta': 25,
    },
    {
        'Pergunta': 'Quanto é 2 / 2?',
        'Opções': [2, 5, 4, 8, 1],
        'Resposta': 1,
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
    print()

    escolha = input('Escolha uma opção:')

    acertou = False
    escolha_int= None
    qtd_opcoes = len(opcoes)
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
               acertou = True    

    if acertou:
        print('Acertou!')
        qtd_acertos += 1
    else: 
        print('Errou.')

if qtd_acertos == len(perguntas):
    print('Você acertou todas as perguntas! Parabéns!')
elif qtd_acertos < len(perguntas) and qtd_acertos > 0:
    print(f'Sua quantidade de acertos foi: {qtd_acertos}. Muito bem!')
else:
    print('Você errou todas as perguntas. Melhore!')


