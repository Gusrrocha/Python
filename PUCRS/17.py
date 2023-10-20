while True:
    soma = 0
    m = int(input("Insira um valor par: "))
    if m % 2 == 0:
        n = int(input("Insira um valor par: "))
        if n % 2 == 0:
            for i in range(m,n+1):
                soma += i
            print("Soma dos números: ", soma)
        else:
            print("Insira novamente os valores (PAR)")
            continue
    else:
        print("Insira novamente o valor (PAR):")
        continue
