amarz = 0
contador = 0
print("Esse é um programa que calcula média aritmética de números pares\n")
while True:
    num = int(input("Insira um número par (0 encerra o programa): "))
    if num == 0:
        print("Você saiu do programa!")
        break
    if num % 2 == 0:
        amarz += num
        contador += 1
print("Calculando...")
if (amarz != 0):
    media = amarz/contador 
    print("A média dos números informados é: ", media)
elif amarz == 0:
    print("Você não inseriu nenhum número par, portanto não tem média.")
