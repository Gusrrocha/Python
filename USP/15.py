intervalo = 0
for x in range(10):
    num = int(input("Insira um número: "))
    if num >= 30 and num <= 90:
        intervalo += 1
print("Quantidade de números entre 30 e 90: ", intervalo)