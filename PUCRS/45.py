med_id = 0
med_alt = 0
med_id_h = 0
pessoas = 0
q = 0
q_mul = 0
q_h = 0
for i in range(2):
    sexo = int(input("Insira sexo (0-feminino, 1-masculino): "))
    idade = int(input("Insira idade: "))
    altura = int(input("Insira altura (cm): "))
    if sexo == 0:
        med_alt += altura
        q_mul += 1
    if sexo == 1:
        med_id_h += idade
        q_h += 1
    if idade in range(18,36):
        pessoas += 1
    med_id += idade
    q += 1
print("\nMédia idade do grupo: ", med_id/q)
print("Média da altura das mulheres: ", med_alt/q_mul)
print("Média da idade dos homens: ", med_id_h/q_h)
print("Percentual de pessoas com idade [18,35]: ", (pessoas/q)*100)

