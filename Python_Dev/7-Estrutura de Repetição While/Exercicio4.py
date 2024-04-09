#Faça uma tabuada

try:
    tabuada = int(input("Informe a tabuada: "))
    i = 0

    while(i < 10):
        i += 1
        print(f'{tabuada} X {i} = {tabuada*i}')

except ValueError:  # É mais específico capturar ValueError aqui
    print('Informe um número inteiro')