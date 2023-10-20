soma, maior, menor, quant_pos, quant_neg = 0,0,0,0,0
for i in range(10):
    num = float(input("Insira um valor real: "))
    if i == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if num >= 0:
        quant_pos += 1
    if num < 0:
        quant_neg += 1
    soma += num
med = soma/10
print("\nA média dos elementos é: ", med)
print("O maior dos elementos é: ", maior)
print("O menor dos elementos é: ", menor)
print("A quantidade de elementos positivos é: ", quant_pos)
print("A quantidade de elementos negativos é: ", quant_neg)
