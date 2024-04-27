#Separe as String
#Junte duas estring
#Remova os espaços vazios

lista_valores = "Ola bom dia, vamos aprender Python"
nova_lista = lista_valores.split(',')
print(10*'-')
print(nova_lista)

print(10*'-')
lista_add = []
for i, palavra in enumerate(nova_lista):
    print(nova_lista[i].strip())

print(10*'-') 
lista_add=(' -').join(nova_lista)
print(lista_add) 