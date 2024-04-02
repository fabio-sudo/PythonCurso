#Receba dois número do usuário aleatórios
#Mostre o maior numero digitado

primerio_numero=int(input("Informe o primeiro número: "))
segundo_numero=int(input("Informe o segundo número: "))

if(primerio_numero > segundo_numero):
    print(f"Maior número foi o primeiro: {primerio_numero}")
elif(primerio_numero < segundo_numero):
    print(f"Maior número foi o segundo: {segundo_numero}")
else:
    print("Os números são iguais")
    