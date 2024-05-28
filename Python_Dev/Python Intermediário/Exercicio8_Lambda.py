
mult = lambda x,y: x*y
multiplicacao = lambda *args: [item for item in args]


result = mult(3, 4)
print(result)  # Output will be: 12

result = multiplicacao(2, 3, 4)
print(result)  # Output will be: [2, 3, 4]

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

imprimir = lambda: [print(item['nome']) for item in lista]

imprimir()

