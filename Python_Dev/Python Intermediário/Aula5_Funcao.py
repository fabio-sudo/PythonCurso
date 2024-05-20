"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 #esse x é Global

def escopo():
    global x # Essa variável global pode ser utilizada em qualquer lugar do algoritimo
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2 #esse y é escoplo da função só pode ser chamado e utilizado dentro da função
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)



"""
Escopo de variáveis globais e locais
"""

y = 100
def funcao():
    global y #Utilizando desta forma consegue trabalhar com variveis fora do escopo
    y=200


print(funcao()) 
print(y)   
