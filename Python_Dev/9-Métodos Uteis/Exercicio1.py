#Arredontamento
#Módulo do python decimal

import decimal

nota_primeiro_semestre = 8.1
nota_segundo_semestre = 5.5

#Decimal para numeros muito precisos
#Converte uma strig ou guarda valor exato de um decimal na memória
nota_terceiro = decimal.Decimal('0.1')
nota_quarto = decimal.Decimal('0.7')

print((nota_primeiro_semestre + nota_segundo_semestre))

print((nota_terceiro + nota_quarto))