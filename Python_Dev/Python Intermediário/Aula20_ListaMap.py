# Definição da função 'dobro' que recebe um número 'x' e retorna o dobro desse número.
def dobro(x):
    return x * 2

# Lista de números.
numeros = [1, 2, 3, 4, 5]

# Mapeia a função 'dobro' para cada elemento da lista 'numeros'.
dobros = map(dobro, numeros)

# Converte o resultado do mapeamento em uma lista e imprime.
print(list(dobros))  # Saída: [2, 4, 6, 8, 10]
print(20*'-')

# Definição da função 'soma' que recebe dois números 'x' e 'y' e retorna a soma deles.
def soma(x, y):
    return x + y

# Listas de números.
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]

# Mapeia a função 'soma' para os elementos correspondentes das listas 'numeros1' e 'numeros2'.
somas = map(soma, numeros1, numeros2)

# Converte o resultado do mapeamento em uma lista e imprime.
print(list(somas))  # Saída: [5, 7, 9]