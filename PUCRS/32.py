for i in range(5):
    a = int(input("Insira um valor inteiro positivo para 'a': "))
    b = int(input("Insira um valor inteiro positivo para 'b': "))
    if a < b:
        print(f"Número pares de {a} a {b}: ")
        for z in range(a,b+1):
            if z % 2 == 0:
                print(z)
    