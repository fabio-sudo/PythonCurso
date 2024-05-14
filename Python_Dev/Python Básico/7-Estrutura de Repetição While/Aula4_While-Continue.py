#Continua a estrutura de repetição 
#Pulando algum trecho

contador = 0

while contador < 50:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')