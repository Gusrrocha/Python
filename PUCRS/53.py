cont = 3
num = 4
print("Número primo: ", 1)
print("Número primo: ", 2)
print("Número primo: ", 3)
while True:
    if cont >= 20:
        break
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print("Número primo: ", num)
        cont += 1
    num += 1
