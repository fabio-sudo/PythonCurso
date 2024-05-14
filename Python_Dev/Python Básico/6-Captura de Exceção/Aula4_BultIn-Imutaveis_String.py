"""
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
nome="fabio"
#Fatiamento
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)

#Primeria Maiuscula
print(nome.capitalize())

#Inserir 0 Left
print(nome.zfill(10))