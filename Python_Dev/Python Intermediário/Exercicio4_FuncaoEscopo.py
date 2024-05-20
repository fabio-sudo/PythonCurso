# Variável global
var_global = 0

# Função que modifica a variável global
def modificar_variavel_global(x = 10):
    global var_global
    var_global += x

# Função que recebe a variável global como argumento e a utiliza
def usar_variavel_global(valor):
    print("Valor da variável global:", valor)

# Chamadas das funções
modificar_variavel_global(10)
#Adiciona 10 a variável
var_global += 10
usar_variavel_global(var_global)