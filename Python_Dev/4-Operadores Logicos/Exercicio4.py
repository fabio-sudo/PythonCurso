#Percorrer pequeno texto com in

texto = "Vamos aprender python"
palavra_buscar = input("Palavra a buscar: ")
print(20 * "-")

#IN
if(palavra_buscar in texto):
    print(f"Palavra encontrada: {palavra_buscar}")
else:
    print(f"Palavra não encontrada: {palavra_buscar}")

#Not in
print(20 * "-")
if(palavra_buscar not in texto):
    print("Texto não encontrado!")