produto = 1
for i in range(93,1478):
    for z in range(2, i):
        if (i % z) == 0:
            break
    else:
        print("Número primo: ", i)
        produto *= i
print("Produto dos números primos: ", produto)
            