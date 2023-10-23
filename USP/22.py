med_1, med_2, med_3, med_4, q_1, q_2, q_3, q_4 = 0,0,0,0,0,0,0,0
for x in range(15):
    idade = int(input("Insira idade: "))
    peso  = float(input("Insira peso: "))
    if idade >= 1 and idade <= 10:
        med_1 += peso
        q_1 += 1
    if idade >= 11 and idade <= 20:
        med_2 += peso
        q_2 += 1
    if idade >= 21 and idade <= 30:
        med_3 += peso
        q_3 += 1
    if idade >= 31:
        med_4 += peso
        q_4 += 1    

print("Média dos pesos: ")
if q_1 != 0:
    print("Faixa etária [1,10]:", med_1/q_1)
if q_2 != 0:
    print("Faixa etária [11,20]:", med_2/q_2)
if q_3 != 0:
    print("Faixa etária [21,30]:", med_3/q_3)
if q_4 != 0:
    print("Faixa etária [31+]:", med_4/q_4)