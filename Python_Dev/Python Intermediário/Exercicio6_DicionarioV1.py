# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',#Petgunta
        'Opções': ['1', '3', '4', '5'],#Lista
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


#Percorre o dicionário para fazer a pregunta
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

#Imprime as questões e Recebe a resposta
    opcoes = pergunta['Opções']
    #Enumerate lista itens da lista
    for i, opcao in enumerate(opcoes):
        #Contador numero do indice
        print(f'{i})', opcao)
    print()

    #recebe o valor escolhido
    escolha = input('Escolha uma opção: ')

    #inicializa a variável
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    #somente se escolha foi digita
    if escolha.isdigit():
        escolha_int = int(escolha)

    #só vai entrar aqui se escolha for inteiro
    if escolha_int is not None:
        #valida intervalo de escolha de opções
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        #Emoji Windows + .
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')