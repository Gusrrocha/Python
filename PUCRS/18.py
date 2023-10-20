while True:
    soma = 0
    div = 0
    m = int(input("Insira um valor positivo: "))
    if m % 2 == 0:
        for i in range(1, m+1):
            if m % i == 0:
                print(f"Divisor de {m}: {i}")
                div += 1
    elif m < 10:
        fat = m
        for i in range(1, m):
            fat *= i
        print(f"Fatorial de {m}: ", fat)
    elif m >= 10:
        for i in range(1, m):
            soma += i
        print(f"Soma de 1 até o número {m}: {soma}")



