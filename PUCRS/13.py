num = int(input("Insira o número de valores a serem lidos: "))
for i in range(num):
    numero = int(input("Insira o valor: "))
    fat = numero
    for z in range(1, numero):
        fat *= z
    print(f"Valor lido: {numero}")
    print(f"Fatorial de {numero}! é: ", fat)
