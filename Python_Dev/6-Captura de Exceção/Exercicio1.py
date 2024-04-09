#Exibindo Capitura de Exceção

try:
    print("Tentando executar o bloco de código")
    # Tentativa de divisão por zero, o que causará um erro
    resultado = 10 / 0
except:
    print("Ops! Divisão por zero não é permitida.")
else:
    print("Executado com sucesso!")
finally:
    print("Bloco finally sempre é executado.")