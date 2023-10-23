q_sim, q_nao, q_mul_s, q_hom_n, q_hom = 0,0,0,0,0
for x in range(4):
    sexo = input("Sexo (M/F): ")
    resposta = input("Resposta (S/N): ")
    if resposta == 'S':
        q_sim += 1
        if sexo == 'F':
            q_mul_s += 1
    if resposta == 'N':
        q_nao += 1
        if sexo == 'M':
            q_hom_n += 1
    if sexo == 'M':
        q_hom += 1
    

print("Número de respostas com 'Sim': ", q_sim)
print("Número de respostas com 'Não': ", q_nao)
print("Número de mulheres com 'Sim':", q_mul_s)
if q_hom != 0:
    print("Porcentagem de homens que respondeu 'Não' entre os homens:", (q_hom_n/q_hom)*100,"%")

