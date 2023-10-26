par = []
impar = []
c1 = 0
c2 = 0
while True:
    n = int(input("Insira um número inteiro: "))
    if n % 2 == 0:
        if len(par) == 5:
            if c1 == 0:
                print("Lista de números pares cheia!")
        else:
            par.append(n)
        
    else:
        if len(par) == 5:
            if c2 == 0:
                print("Lista de números ímpares cheia!")
        else:
            impar.append(n)
    sair = input("Deseja sair? (s/n): ")
    if sair == 's':
        break

if len(par) < 5:
    print(f"A lista de números pares não foram preenchidas completamente: {par}")
if len(impar) < 5:
    print(f"A lista de números ímpares não foram preenchidas completamente: {impar}")