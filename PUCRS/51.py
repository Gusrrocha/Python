n = int(input("Insira um número inteiro e positivo: "))
fat = n
for i in range(1,n):
    fat *= i
print("O fatorial de", n,"é:", fat)