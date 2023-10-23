med_ot, q_ot, q_reg, q_bom, pes = 0,0,0,0,0
for x in range(15):
    opn = int(input("Opinião sobre o filme (1-Ótimo,2-Bom,3-Regular): "))
    idade = int(input("Idade: "))
    if opn == 1:
        med_ot += idade
        q_ot += 1
    if opn == 2:
        q_bom += 1
    if opn == 3:
        q_reg += 1
    if opn > 3 or opn < 1:
        pass
    else:
        pes += 1
if q_ot != 0:
    print("Média das idades: ", med_ot/q_ot)
print("Regular: ", q_reg)
print("Porcentagem de pessoas que responderam bom:", (q_bom/pes)*100)
