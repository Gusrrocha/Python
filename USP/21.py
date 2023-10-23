n = int(input("Insira um número inteiro: "))
if n == 0:
    print("0! = 1")
else:
    fat = n
    for i in range(1,n):
        fat *= i
    print(f"{n}! = {fat}")
