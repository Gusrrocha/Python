maior = 0
menor = 0
prim = 0
while True:
    valor = int(input("Insira um valor (0 encerra): "))
    if valor == 0:
        break
    elif valor < 0:
        print("Insira um valor positivo...")
    elif valor > 0:
        if prim > 0:
            menor = valor
            prim += 1
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
print("O maior valor é: ", maior)
print("O menor valor é: ", menor)
        
