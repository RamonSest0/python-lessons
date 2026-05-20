"""
Tipo Tupla - Uma lita imutável, portanto não suporta os métodos de list...
Formas de criar : sem [], usando ()
"""

nomes = 'Ramon', 'Ana Julia', ':)'
print(nomes[-1])
print(nomes)

ingredientes = ('arroz', 'feijão', 'batata')
print(ingredientes)

carros = ['March', 'Uno', 'Corsa']
carros = tuple(carros) # coverte list in tuple
carros = list(carros) # converte tuple in list
print(carros)
