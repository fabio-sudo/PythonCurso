#Evitar caracteres especiais como @, #, $, etc.
#Evitar começar com números.
#Escolher nomes descritivos que indiquem claramente o propósito da variável.

#Var string
nome = "Meu Nome"
nome_completo = "Meu Nome Sobrenome"

#Var int
idade = 18

#Var boolean
maior_idade = idade >= 18

#Var float
salario = 1500.00

print("Nome: " + nome +
      "\nIdade: " + str(idade) +  # Convertendo idade para string
      "\nMaior de Idade: " + str(maior_idade) +  # Convertendo maior_idade para string
      "\nSalário: " + str(salario))  # Convertendo salário para string