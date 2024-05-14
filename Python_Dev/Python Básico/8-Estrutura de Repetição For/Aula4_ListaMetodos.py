"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
import os
os.system('cls')
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]

lista.append(50) #Adiciona ao final da lista
lista.pop()#Remove ultimo item lisa

lista.append(60)
lista.append(70)
#Remover Posicao especifica
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)