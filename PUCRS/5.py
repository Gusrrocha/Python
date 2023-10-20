total = 0
contador = 0
while True:
    num = int(input("Insira um valor: "))
    if (num < 0):
        break
    total += num
    contador += 1
med = total/contador
print(f"A média aritmética é: {med:.2f}")
