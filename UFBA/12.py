a = int(input("Insira um valor inteiro (ínicio do intervalo): "))
b = int(input("Insira um valor inteiro (final do intervalo): "))
t = int(input("Tamanho da lista: "))
lista = []
c = 0
for i in range(t):
    num = int(input("Insira um número: "))
    lista.append(num)
    if num in range(a,b+1):
        c += 1
print("Quantidade de elementos dentro da lista:", c)