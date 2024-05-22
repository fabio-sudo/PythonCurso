#*args declara uma turpla (1,2,4,5,6,7,8 ) valores fixos em uma lista

def soma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(soma(1, 2, 3, 4, 5, 6, 7, 8))
