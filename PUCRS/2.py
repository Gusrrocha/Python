num = abs(int(input("Insira um valor: ")))
e = 1
for i in range(1, num+1):
    fat = i
    for z in range(1, i):
        fat *= z
    e += 1/fat
print(e)

