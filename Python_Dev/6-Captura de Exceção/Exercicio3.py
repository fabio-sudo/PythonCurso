#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.

entrada = input('Digite um número: ')

if entrada.isdigit():  # Verifica se a entrada é um número
    entrada_int = int(entrada)

    if entrada_int % 2 == 0:  # Verifica se o número é par
        print(f'Número Par: {entrada_int}')
    else:
        print(f'Número Ímpar: {entrada_int}')

else:
    print('Informe o valor corretamente')


