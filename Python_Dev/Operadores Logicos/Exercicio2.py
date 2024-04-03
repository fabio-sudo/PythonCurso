#Recebe E para entrar S para sair
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
else:
     print('Sair')

# Se verdadeiro recebe a senha Se Falso retorna Sem senha
#Avaliação curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)