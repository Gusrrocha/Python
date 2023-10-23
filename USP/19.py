q = 0
media = 0
while True:
    idade = abs(int(input("Insira idade (0 encerra): ")))
    if idade == 0:
        break
    media += idade
    q += 1
print("A média das idades é: ", media/q)

