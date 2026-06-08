"""
Operação ternária (condicinal de uma linha)
<valor> if <condicao> else <outra valor>
"""

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 12
novo_digito = digito if digito <= 9 else 0
print(novo_digito)