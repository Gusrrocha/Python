soma = 0
print("\nNúmeros negativos somam!")
while True:
    num = int(input("Insira um número inteiro: "))
    if num == 0:
        break
    if num < 0:
        soma += num
print("Resultado da soma de números negativos: ", soma)
    
