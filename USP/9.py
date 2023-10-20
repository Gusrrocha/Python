num = int(input("Digite o número que deseja visualizar a sua tabuada: "))
print(f"Tabuada de {num}:")
for i in range(1,11):
    print(f"{num} x {i}: ", num*i)