def tabuada(base, linhas):
    i = 1
    while i <= linhas:
        resultado = base * i
        print(f"{base} x {i} = {resultado}")
        i += 1

base = int(input("Informe a Base: "))
linhas = int(input("Informe as linhas: "))

tabuada(base, linhas)