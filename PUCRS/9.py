maior = 0
menor = 0
for i in range(50):
    num = float(input("Insira um valor: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("O maior valor inserido é: ", maior)
print("O menor valor inserido é: ", menor)
