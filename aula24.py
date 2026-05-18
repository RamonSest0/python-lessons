"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
(caractere)(><^)(quantidade)
> direita
< esquerda
^ centro
Sinal - + ou - 
Ex.: 0>-100,.1f
Coversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:0>10}')
print(f'{variavel:0^7}')
print(f'{variavel:0<10}')
print(f'O hexadecimal de 1500 é {1500:08x}')

