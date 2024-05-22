def multiplica(*args):
    total = 1  # Inicializa total com 1
    for arg in args:
        total *= arg  # Multiplica cada argumento ao total
    return total

print(multiplica(1, 2, 3, 4, 5, 6, 7, 8))