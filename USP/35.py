som_p = 0
neg_p = 0
while True:
    pos = abs(int(input("Insira um número positivo (0 encerra): ")))
    if(pos== 0):
        break
    while True:
        neg = int(input("Insira um número negativo: "))
        if neg < 0:
            break
        else:
            print("Insira um número negativo.")
    som_p += pos
    neg_p += neg
print("Soma dos positivos:", som_p)
print("Soma dos negativos:", neg_p)
print("Soma das parcias: ", som_p+neg_p)
