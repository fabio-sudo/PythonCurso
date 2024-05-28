pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

#------------Desempacotando juntando listas
pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)
print(20*'-')
#--------------------args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print('Nomeados: '+chave, valor)


mostro_argumentos_nomeados(nome='Joana', qlq=123)
print(20*'-')
mostro_argumentos_nomeados(**pessoas_completa)
print(20*'-')

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)