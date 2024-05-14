# Solicita ao usuário para inserir sua idade
idade = int(input("Qual é a sua idade? "))

# Define a idade mínima para dirigir
idade_minima_para_dirigir = 18

# Verifica se a pessoa pode dirigir com base na idade
if idade >= idade_minima_para_dirigir:
    print("Você pode dirigir!")
else:
    anos_que_faltam = idade_minima_para_dirigir - idade
    print(f"Desculpe, você ainda não pode dirigir. Você precisa esperar mais {anos_que_faltam} anos.")