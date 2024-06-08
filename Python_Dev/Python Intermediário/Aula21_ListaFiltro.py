import pprint

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para filtrar números pares
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Filtrando números pares
pares = filtrar_pares(numeros)

# Imprimindo a lista filtrada de forma legível usando pprint
print("Lista de números pares:")
pprint.pprint(pares)