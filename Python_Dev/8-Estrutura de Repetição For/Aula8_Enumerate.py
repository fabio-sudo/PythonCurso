#Enumera uma lista com seus indices
import os
os.system('cls')


lista = ["Fábio", "Sofia", "Natália"]

#Só percorre uma vez desta forma a lista Ponteiro ultima posição
lista_enumerate = enumerate(lista)

for item in lista_enumerate:
    print(item)

#Maneira correta
for item in enumerate(lista):
    print(item)