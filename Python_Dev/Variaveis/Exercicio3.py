
#F strings
nome = 'Fábio'
altura = 1.79
peso = 90
imc = peso / altura ** 2

print(f'{nome} tem altura de altura')
print(f'pesa {peso} quilos e seu imc é')
print(f'{imc:.2f}')

#Formate
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)