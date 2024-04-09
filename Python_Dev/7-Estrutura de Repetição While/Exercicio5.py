#Descobrir quantas vezes uma letra apareceu

texto = "Hoje é dia de programar em python"
texto.lower()

while True:
    i = 0
    quantidade = 0

    letra = input("Escreva uma letra: ")
    letra.lower()

    while i < len(texto):
               
        if(letra == texto[i]):
            quantidade += 1

        i += 1

    #informa quantidade de repetição
    print(f"Quantidade de repetição: {quantidade} ")

    #Verifica se quer finalizar o loop
    if(input("Deseja continar [s]im ou [n]ão") != "s"):
        break

print("Você saiu")