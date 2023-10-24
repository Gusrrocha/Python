q_alt = 0
soma = 0
while True:
    idade = int(input("Idade: "))
    if idade < 0:
        break
    altura = int(input("Altura em cm: "))
    if idade > 50:
        soma += altura
        q_alt += 1
print("Média das alturas em cm:",soma/q_alt)