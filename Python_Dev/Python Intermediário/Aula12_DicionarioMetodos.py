p1 = {
    'nome': 'Steve',
    'sobrenome': 'Jobs',
}

#Caso nome estiver vazio exibe uma menssagem
print(p1.get('nome','Não tem nome'))

#remove item do dicionário
nome = p1.pop('nome')
print(nome)
print(p1)

#Lista de dicionários
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)


pessoa = {
    'nome': 'Fábio Henrique',
    'sobrenome': 'Trevezane',
    'idade': 32,
}


# setdefault - adiciona uma chave com um valor padrão se a chave não existe
pessoa.setdefault('idade', 0)
print("Valor associado à chave 'idade' após setdefault:", pessoa['idade'])
print(10*'-')
# len - retorna o número de chaves no dicionário
print("Número de chaves no dicionário:", len(pessoa))
print(10*'-')
# keys - retorna uma lista contendo as chaves do dicionário
print("Chaves do dicionário como lista:", list(pessoa.keys()))
print(10*'-')
# values - retorna uma lista contendo os valores do dicionário
print("Valores do dicionário como lista:", list(pessoa.values()))
print(10*'-')
# items - retorna uma lista de tuplas contendo pares (chave, valor) do dicionário
print("Pares chave-valor do dicionário como lista de tuplas:", list(pessoa.items()))
print(10*'-')
# Imprime valores de dentro do dicionário
for valor in pessoa.values():
    print(valor)
print(10*'-')
# imprime a chave e valor do dicionário
for chave, valor in pessoa.items():
    print(chave, valor)
print(10*'-')
# copy - cria uma cópia rasa (shallow copy) do dicionário
copia_pessoa = pessoa.copy()
print("Cópia rasa do dicionário:", copia_pessoa)
print(10*'-')
# get - obtém o valor associado a uma chave, retornando um valor padrão se a chave não existe
valor_idade = pessoa.get('idade')
print("Valor associado à chave 'idade':", valor_idade)
print(10*'-')
# pop - remove e retorna o valor associado a uma chave especificada
valor_removido = pessoa.pop('sobrenome')
print("Valor removido associado à chave 'sobrenome':", valor_removido)
print("Dicionário após o pop:", pessoa)
print(10*'-')
# popitem - remove e retorna o último par chave-valor adicionado ao dicionário
ultimo_par_removido = pessoa.popitem()
print("Último par chave-valor removido:", ultimo_par_removido)
print("Dicionário após popitem:", pessoa)
print(10*'-')
# update - atualiza o dicionário com outro dicionário ou com pares chave-valor
novos_valores = {'idade': 33, 'cidade': 'São Paulo'}
pessoa.update(novos_valores)
print("Dicionário atualizado após update:", pessoa)
