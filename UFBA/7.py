lista = []
par = 0
for i in range(10):
    n = int(input("Insira número inteiro: "))
    lista.append(n)
    if n % 2 == 0:
        par += 1

print("Elementos da lista:")
for item in lista:
    print(item)
print(f"\nExistem {par} números pares.")