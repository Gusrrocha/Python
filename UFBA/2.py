lista = []
for i in range(10):
    num = int(input("Insira um valor inteiro: "))
    lista.append(num)
adv = int(input("Informe um número: "))
if adv in lista:
    print("O número informado está na lista.")
else:
    print("O número informado não está na lista")
