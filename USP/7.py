contador = 0
for i in range(10):
    idade = int(input("Digite a idade da pessoa: "))
    if idade >= 18:
        contador +=1
print(f"Com base nos dados informados, tem {contador} pessoas com idade maior/igual a 18 anos!")