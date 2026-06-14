# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

total_mult = mult(3, 6, 3, 9, 1, 3)
print(total_mult)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(num):
    verif = num % 2 == 0
    
    if verif:
        return f'O número {num} é par.'
    else:
        return f'O número {num} é ímpar.'
    
result_par_impar = par_ou_impar(3)
print(result_par_impar)

