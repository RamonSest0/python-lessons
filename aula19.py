"""
Operadores lógicos
and (e) or (or) not (não)
and - Todas a condições precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor 
São consideras falsy: 0 0.0 '' False
Também existe o tipo None que é usado para reprensentar um não valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input ('Senha: ')

senha_permitida = '12345678'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou! :)')
else:
    print('Saiu')