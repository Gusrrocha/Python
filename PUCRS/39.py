
num = 1
cont = 0
c = 1

while cont < 5:
    verifier = 0
    num += 2**c
    for i in range(2,num):
        if (num % i) == 0:  
            break   
    else:
        print(f"{cont+1}º Número perfeito: ", 2**c*num)
        cont += 1
    c += 1