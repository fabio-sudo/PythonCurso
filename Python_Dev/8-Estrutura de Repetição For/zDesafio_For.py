class Aluno:
    def __init__(self, identificador, nome, sobrenome, idade):
        self.id = identificador
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


# Criar alguns objetos Aluno
aluno1 = Aluno(1, "João", "Silva", 20)
aluno2 = Aluno(2, "Maria", "Santos", 21)
aluno3 = Aluno(3, "Pedro", "Ferreira", 22)

# Criar uma lista de alunos e adicionar os objetos Aluno à lista
lista_alunos = [aluno1, aluno2, aluno3]

id_buscar = int(input("Digite o ID do Aluno: "))

#Percorre a lista de alunos
for aluno in lista_alunos:
    if(id_buscar == aluno.id):
        print(f' ID: {aluno.id} \n Nome: {aluno.nome} \n Idade: {aluno.idade}')
        break
else:
    print("ID não encontrado!")
   