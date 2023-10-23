idade_ac = 0
q_1030 = 0
q_peso = 0
q_pessoas = 0
for x in range(10):
    idade = int(input("Insira a idade da pessoa: "))
    altura = int(input("Insira a altura em cm: "))
    peso = float(input("Insira o peso da pessoa (kg): "))
    
    if idade >= 10 and idade <= 30 and altura > 190:
        q_1030 += 1
    if peso > 90 and altura < 150:
        q_peso += 1
    idade_ac += idade
    q_pessoas += 1
print("Média da idade: ",idade_ac/q_pessoas)
print("Quantidade de pessoas com peso maior que 90kg e altura menor que 150cm: ", q_peso)
print("Porcentagem de pessoas com idade entre 10 e 30 anos e que tem mais de 190cm de altura: ", q_1030/q_pessoas)