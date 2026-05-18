palavra_secreta = 'pimpolho' # aqui definimos a palavra secreta
letras_acertadas = '' # fora do loop para gravar as letras acertadas até o momento
contagem_tentativas = 0 # também fora do loop para gravar as tentativas

while True: # while True, só é quebrado quando o usuário acerta uma letra da palavra secreta

    palavra_formada = '' # dentro do loop para que seja resetada a cada rodada
    palpite = input('Existe uma palavra secreta. Digite uma letra, para ver se ela aparece na palavra secreta: ')

    if palpite == ' ' or palpite == '': # verifica se há espaços ou se nada foi digitado. Se sim, laço continua
        contagem_tentativas += 1
        print('Caractere inválido. Tente novamente.')
        continue

    if len(palpite) > 1: # verifica se foi digitada mais de uma letra
        print('Digite apenas uma letra.')
        contagem_tentativas += 1
        continue

    if palpite.lower() in palavra_secreta.lower(): # verifica se o palpite está na palavra secreta
        letras_acertadas += palpite # adicona o palpite nas letras acertada até o momento

    for letra in palavra_secreta: # aqui montamos a palavra percorrendo a palavra secreta
        if letra.lower() in letras_acertadas.lower(): # verificamos se a letra atual no for está nas letras acertadas
            palavra_formada += letra # se estiver adiconamos a letra
        else:
            palavra_formada += '*' # se não estiver colocamos * 

    print(palavra_formada) # palavra montada no loop for ^
    contagem_tentativas += 1 

    if palavra_formada == palavra_secreta: # verifica se a palavra formada é igual a palavra secreta, ou seja, e todas as letra foram acertadas
        print(f'Parabéns, você venceu! Você precisou de {contagem_tentativas} tentativas.')
        break

print('fim do laço') # apenas para exercício mental indicando o fim do laço
