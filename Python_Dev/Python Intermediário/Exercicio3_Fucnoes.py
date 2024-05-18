#Faça a divisão 
#Faça a subtração
import os

os.system("cls")

#é possível inicializar os parâmetros
def divisao(x , y, z = 0):
   print(f"{x} / {y} = {x/y}")

def subtracao(x, y):
   print(f"{x} - {y} = {x-y}")

#é possível informar a variavel que recebe o parametro
divisao(x=10,y=2)
subtracao(10,2)