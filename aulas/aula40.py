"""
+ - concatena listas
extend - estende a lista
"""

# + 

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

# extend()

lista_d = lista_a.extend(lista_b) # extend() realiza uma ação, mas não retorna nada. 
print(lista_d) # Por isso lista_d = None
print(lista_a) # podemos ver que extend() realizou a ação devida na lista_a
