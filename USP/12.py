i_superior = 0
alt_1020 = 0
q_1020 = 0
q_peso = 0
q_pessoas = 0
for x in range(25):
    idade = int(input("Insira a idade da pessoa: "))
    altura = int(input("Insira a altura em cm: "))
    peso = float(input("Insira o peso da pessoa (kg): "))
    if idade > 50:
        i_superior += 1
    if idade >= 10 and idade <= 20:
        alt_1020  += altura
        q_1020 += 1
    if peso < 40:
        q_peso += 1
    q_pessoas += 1
print("Quantidade de pessoas com mais de 50 anos: ", i_superior)
print("Média das alturas de pessoa com 10 a 20 anos de idade: ", alt_1020/q_1020)
print("Porcentagem de pessoas com peso menor que 40kg: ", (q_peso/q_pessoas)*100)
