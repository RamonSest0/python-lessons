num_int = input('Digite um número inteiro: ')

try:
    conversao_int = int(num_int) # conversao para int
    par_impar = conversao_int % 2 #adquirindo resto

    if par_impar == 0: # verficando se par ou impar
        print('O número digitado é par.')
    else: 
        print('O número digitado é ímpar.')

except: # se der erro ao converter para int
    print('Desculpe, o que você digitou não é um número inteiro.')
