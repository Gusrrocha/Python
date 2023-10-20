while True:
    conjunto = set()
    for i in range(20):
        num = int(input(f"Insira um número (diferente)[{i+1}/20]: "))
        conjunto.add(num)
    print("{:<15} {:<15} {:<15} {:<15}".format("Número", "Quadrado", "Cúbico", "Raiz Quadrada"))
    print("-----------------------------------------------------------------------------------------------")
    for i in conjunto:
        print("{:<15} {:<15} {:<15} {:<15}".format(i, i**2, i**3, i**(1/2)))
    conjunto.clear()
    cont = input("Insira qualquer tecla para continuar: ")
