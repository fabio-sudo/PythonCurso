
import os
os.system('cls')
#        0   1   2   3   
lista = [10, 20, 30, 40]

#Recebe dois parâmetros posição e valor a add
lista.insert(0,5)
print(lista)

#Concatenando Lista
listaA = [1,2,3,4,5]
listaB = ['a','b','c','d','e'] 
listaC = listaA + listaB
listaA.extend(listaB)#Adiciona os valores da lista B na lista A
print(listaC)
