#Funções em Python
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

#Informações para o usuário
print("Operações disponíveis:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

#Estrutura de repetição While True -> roda até que break execute
while True:
        escolha = input("Escolha a operação (1/2/3/4): ")

        if escolha not in ('1', '2', '3', '4'):
            print("Entrada inválida. Por favor, escolha um número entre 1 e 4.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicao(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

        elif escolha == '4':
            resultado = divisao(num1, num2)

            if resultado == "Erro! Divisão por zero.":
                print(resultado)

            else:
                print(f"{num1} / {num2} = {resultado}")

        nova_operacao = input("Deseja fazer outra operação? (sim/não): ")
        if nova_operacao.lower() != 'sim':#Lower deixa Maiusculo
            break
