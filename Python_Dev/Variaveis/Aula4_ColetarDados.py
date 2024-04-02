#Função input para receber os valores do usuário.
#Os valores são coletados em forma de texto.
#Para realizar algum calculo com os mesmo é necessário realizar a conversão

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')