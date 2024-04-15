#Utilizar o FOR para exibir listas
import os
os.system('cls')
lista_nome = ["Fábio","Lucas","Ricardo"]
#sendo usada para criar uma sequência de números que corresponde aos índices da lista 
indice = range(len(lista_nome))

for i in indice:
    print(f"Indice: {i} - {lista_nome[i]}")    