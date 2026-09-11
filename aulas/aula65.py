# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

s1 = set() # set vazio
s1 = {'Ramon', 1, 2, 3, 4} # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s2 = {1, 2, 3, 4, 4, 4, 5} # elimina valores duplicados
print(s2)

l1 = [1, 2, 3, 4, 4, 4, 4, 5]
s3 = set(l1)
l2 = list(s3)
print(l2)

# Métodos úteis:
# add, update, clear, discard
s4 = set()
s4.add('Ramon')
s4.add(1)
s4.update(('Olá, Mundo', 1, 2, 3, 4))
# s4.clear() 
s4.discard('Olá, Mundo')
print(s4)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s5 = {1, 2, 3}
s6 = {2, 3, 4}
s7 = s5 | s6
s8 = s5 & s6
s9 = s6 - s5
s10 = s5 ^ s6
print(s10)