faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
for i in range(15):
    idade = int(input("Insira a idade da pessoa: "))
    if idade <= 15:
        faixa1 += 1
    if idade >= 16 and idade <= 30:
        faixa2 += 1
    if idade >= 31 and idade <= 45:
        faixa3 += 1
    if idade >= 46 and idade <= 60:
        faixa4 += 1
    if idade >= 61:
        faixa5 += 1
print(f"Tem {faixa1} pessoas na faixa de até 15 anos!")
print(f"Tem {faixa2} pessoas na faixa de 16 a 30 anos!")
print(f"Tem {faixa3} pessoas na faixa de 31 a 45 anos!")
print(f"Tem {faixa4} pessoas na faixa de 46 a 60 anos!")
print(f"Tem {faixa5} pessoas na faixa de acima de 61 anos!")
soma = faixa1 + faixa5
total = faixa1 + faixa2 + faixa3 + faixa4 + faixa5
porcentagem = (soma/total)*100
print(" ")
print(f"A porcentagem de pessoas na primeira e última faixa etária com relação ao total de pessoas é: {porcentagem:2f} %")         