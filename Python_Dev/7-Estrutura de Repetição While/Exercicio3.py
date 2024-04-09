#Utilize o While para soletrar o seu nome

nome="Fábio"
novo_nome = ""
tamanho_nome = len(nome)
contador = 0

while contador < tamanho_nome:

    #print(nome[contador], sep="-")
    novo_nome += nome[contador] + " "
    contador += 1

print(novo_nome)