#Utilizando o NOT
senha   = input('Senha: ')

if not senha:
    print("Senha vazia!")
elif senha == "123":
    print("Senha Correta")

#Inverte o retorno
print(not True)