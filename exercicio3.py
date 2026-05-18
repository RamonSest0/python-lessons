horas = input('Que horas são? ')

try:
    horas_int = int(horas)

    if horas_int >= 0 and horas_int <= 11:
        print('Bom dia')
    elif horas_int >= 12 and horas_int <= 17:
        print('Boa tarde')
    elif horas_int >= 18 and horas_int <= 23:
        print('Boa noite')
    else: 
        print('Hora inválida')
        
except:
    print('Você não digitou um número')
