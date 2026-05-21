"""
Exercício
Exiba os índices da lista

Quando usamos range()?

Quando queremos:

repetir algo várias vezes
trabalhar com números
controlar repetições
"""

lista = ['Ramon', 'Ana Julia', 'AR']

indices = range(len(lista)) # aula 34

for i in indices:
    print(f'{lista[i]} está no índice {i}')