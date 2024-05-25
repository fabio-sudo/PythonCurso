perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
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

qtd_acertos = 0

for pergunta in perguntas:
    i = 0
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for opcao in pergunta['Opções']:
        print(f'{i} {opcao}')
        i+=1
    print()
    escolha = input('Escolha uma opção: ')

    try:
        escolha_int = int(escolha)
        if pergunta['Opções'][escolha_int] == pergunta['Resposta']:
            print('Acertou 👍')
            qtd_acertos += 1
        else:
            print('Errou ❌')
    except (ValueError, IndexError):
        print('Escolha inválida. Digite o número correspondente à sua escolha.')
    print()

print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')