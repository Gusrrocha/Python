q_pessoas = 0
q_peso = 0
idade_ac = 0
for i in range(7):
    idade = int(input("Idade da pessoa: "))
    peso = float(input("Peso da pessoa em kg: "))
    
    if peso > 90:
        q_peso += 1

    idade_ac += idade
    q_pessoas += 1

print("Pessoas com mais de 90 quilos: ", q_peso)
print("Média da idade: ", idade_ac/q_pessoas)
    