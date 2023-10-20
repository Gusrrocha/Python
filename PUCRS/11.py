n = int(input("Insira o número de termos: "))
a1 = int(input("Insira o primeiro termo: "))
r = int(input("Insira a razão da P.A: "))
soma = 0
for i in range(1,n+1):
    termo = a1+(i-1)*r
    soma += termo
    print(f"{i}º termo é: ", termo)
print("A soma dos termos é: ", soma)