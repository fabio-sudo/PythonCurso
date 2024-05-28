#Cria uma lista vazia
lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

#Outra modelo de passar valores para uma lista
lista2 = list(range(10))
print(lista2)

#Outra modelo de passar valores para uma lista
lista3 = [numero for numero in range(10)]
print(lista3)