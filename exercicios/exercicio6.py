while True:

    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ') 

    numero_1_float = 0
    numero_2_float = 0
    
    # fazer conversão dos números de entrada
    try: 
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        print('Você digitou um ou dois números inválidos. Tente novamente.')
        numeros_validos = False
        continue

    operador = input('Digite um operador (+-*/)')

    # verificar se foi digitado mais de um operador
    if len(operador) > 1: 
        print('Você digitou mais de um operador.')
        continue

    # verificando se o operador digitado é válido
    if operador not in '+-*/':
        operador_valido = False
        print('Operador inválido. Tente novamente.')
        continue

    print('Realizando operação...')

    if operador == '+':
            print(f'{numero_1_float} + {numero_2_float}', numero_1_float + numero_2_float)
    elif operador == '-':
            print(f'{numero_1_float} - {numero_2_float}', numero_1_float - numero_2_float)
    elif operador == '*':
            print(f'{numero_1_float} * {numero_2_float}', numero_1_float * numero_2_float)
    elif operador == '/':
            print(f'{numero_1_float} / {numero_2_float}', numero_1_float / numero_2_float)
    else:
            print('Deu algum bigode aí...')

    sair = input('Sair? [s]im [n]ão: ').lower().startswith('s')

    if sair:
        print('Você saiu.')
        break
    else:
        print('Reiniciando')
        continue