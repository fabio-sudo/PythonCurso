#Lista de compras
import os

#Lista Vazia
lista = []


while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')
    try:
        if opcao == 'i':
            os.system('cls')#limpa dados
            item = input('Item: ')
            lista.append(item)
        
        elif opcao == 'a':
            os.system('cls')
            print('Limpando Lista...')
            lista.clear()
            print('Lista limpa com sucesso.')
        
        elif opcao == 'l':
            os.system('cls')#limpa dados
            print('Lista de Items: ')
            for item in enumerate(lista):
                print(item)
        
        elif opcao == 's':
            os.system('cls')#limpa dados
            break

        else:
            print('Opção inválida.')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')       