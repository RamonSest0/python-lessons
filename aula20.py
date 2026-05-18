# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input ('Senha: ')

# senha_permitida = '12345678'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrou! :)')
# else:
#     print('Saiu')

# avaliação de curto circuito

# e um valor for considerado verdadeiro, toda operação será considerada verdadeira. Apenas o priemiro valor verdadeiro é considerado

print(False or 1 or True)

senha = input('Senha: ') or 'abc' 
print(senha)