"""
se você tem uma lista de números e deseja remover os duplicados,
 pode convertê-la em um conjunto usando set().
"""
lista = [1, 2, 3, 4, 1, 2, 5]
conjunto = set(lista)
print(conjunto)  # Saída: {1, 2, 3, 4, 5}


"""
Python suportam operações de conjuntos,
como união, interseção e diferença. 
Isso pode ser útil em muitos cenários, 
como encontrar elementos comuns em duas coleções, 
remover elementos duplicados ou encontrar elementos exclusivos em diferentes conjuntos.
"""
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União
uniao = A.union(B)
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Interseção
intersecao = A.intersection(B)
print(intersecao)  # Saída: {3, 4}

# Diferença
diferenca = A.difference(B)
print(diferenca)  # Saída: {1, 2}