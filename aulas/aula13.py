nome = 'Ramon'
altura = 1.67
peso = 57.5
imc = peso / altura ** 2 

# f (formatting) string nos ajuda a formatar melhor o texto sem tanto uso de , e +
print(f'{nome} tem {altura} de altura e pesa {peso} quilos.')
print(f'Seu IMC é: {imc:.2f}') # podemos definir quantas casas decimais queremos
# usando f string