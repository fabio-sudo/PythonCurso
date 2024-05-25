def remover_duplicatas(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

# Teste da função
lista_original = [1, 2, 3, 4, 1, 2, 5]
resultado = remover_duplicatas(lista_original)
print("Lista original:", lista_original)
print("Lista sem duplicatas:", resultado)