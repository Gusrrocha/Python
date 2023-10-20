lista = []
for i in range(5):
    for z in range(4):
        num = int(input(f"Insira um valor para o Grupo {i+1}: "))
        print(num)
        lista.append(num)
    lista.sort()
    print(f"Grupo {i+1} (crescente): ", lista)
    lista.sort(reverse=True)
    print(f"Grupo {i+1} (decrescente): ", lista)
    lista.clear()