
n = int(input("Insira número: "))
for i in range(n):
    num = int(input("Insira o número para ver seu fatorial: "))
    fat = num
    print("{:<15} {:<15}".format("Número", "Fatorial"))
    for z in range(1, num):
        fat *= z
    print("{:<15} {:<15}".format(num, fat))