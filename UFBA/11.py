while True:
    lista = []
    for i in range(15):
        num = int(input("Insira um número real: "))
        lista.append(num)
    print("1. Imprimir lista de forma direta")
    print("2. Imprimir lista de forma inversa")
    print("0. Sair")
    cod = int(input("Insira o código númerico: "))
    if cod == 0:
        break
    if cod == 1:
        for item in lista:
            print(item)
    elif cod == 2:
        lista.reverse()
        for item in lista:
            print(item)