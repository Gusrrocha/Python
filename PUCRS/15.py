intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
while True:
    num = float(input("Digite um número (negativo encerra o programa): "))
    if num < 0:
        break
    if num <= 25:
        intervalo1 += 1
    if num > 25 and num <= 50:
        intervalo2 += 1
    if num > 50 and num <= 75:
        intervalo3 += 1
    if num > 75 and num <= 100:
        intervalo4 += 1
print("Quantidade de números no intervalo [0,25]: ", intervalo1)
print("Quantidade de números no intervalo [26,50]: ", intervalo2)
print("Quantidade de números no intervalo [51,75]: ", intervalo3)
print("Quantidade de números no intervalo [76,100]: ", intervalo4)