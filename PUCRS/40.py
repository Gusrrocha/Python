n = int(input("Insira um valor: "))
for i in range(n):
    soma = 0
    m = int(input("\nInsira um valor inteiro e positivo: "))
    fat = m
    for z in range(1, m):
        soma += z
    for z in range(1, m):
        fat *= z
    print("\n{:<15} {:<15} {:<15}".format("Valor", "Somatório", "Fatorial"))
    print("{:<15} {:<15} {:<15}".format(m, soma, fat))