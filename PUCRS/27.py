maior_valor = 0
menor_valor = 0
med = 0
cont = 0
for i in range(10):
    num = int(input("Insira 500 valores inteiros e positivos: "))
    if i == 0:
        menor_valor = num     
    elif num < menor_valor:
        menor_valor = num
    if num > maior_valor:
        maior_valor = num
    med += num
    cont += 1
print("O maior valor é: ", maior_valor)
print("O menor valor é: ", menor_valor)
print("A média é: ", med/cont)