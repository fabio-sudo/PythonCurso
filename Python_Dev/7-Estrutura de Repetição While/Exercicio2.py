"""
Faça uma contagem de 0 a 100
e pule o 50
e pare a execução no 90
"""

contador = 0

while contador < 100:
    contador+=1

    if(contador == 50):
        continue

    if(contador == 90):
        break

    print(contador)