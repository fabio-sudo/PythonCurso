"""
For + Range
range -> range(start, stop, step)

Define um intervalo de números usando a função range. Esta função range é chamada com três parâmetros:

start=0: o intervalo começa em 0.
stop=50: o intervalo vai até, mas não inclui, 50.
step=5: os números no intervalo aumentam de 5 em 5.
"""
numeros = range(0, 50, 5)

for numero in numeros:
    print(numero)