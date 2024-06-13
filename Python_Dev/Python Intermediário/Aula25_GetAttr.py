lista = [1, 2, 3]
print(dir(lista))


string = 'Luiz'
if hasattr(string, 'strip'):
    print('A string tem o método strip')

string = 'Luiz'
metodo = 'strip'
if hasattr(string, metodo):
    print(getattr(string, metodo)())


# Define uma string
string = 'Fábio'

# Define o método a ser verificado
metodo = 'strip'

# Verifica se o objeto 'string' possui o método especificado em 'metodo'
if hasattr(string, metodo):
    # Se o método existe, imprime que ele existe
    print('Existe upper')
    
    # Obtém o método especificado em 'metodo' e o executa, em seguida imprime o resultado
    print(getattr(string, metodo)())
else:
    # Se o método não existe, imprime que ele não existe
    print('Não existe o método', metodo)