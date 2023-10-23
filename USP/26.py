soma = 0
contador = 0
while True:
    idade = int(input("Insira idade (0 encerra): "))
    if idade == 0:
        break
    elif idade < 0:
        print("Insira idades positivas.")
        continue
    soma += idade
    contador += 1
print("Média das idades:", soma/contador)