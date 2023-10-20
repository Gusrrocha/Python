cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0
while True:
    voto = int(input("Insira o código de seu voto (1 a 6)(0 encerra o programa): "))
    if voto == 0:
        print("Você saiu do programa!")
        break
    if voto < 0 or voto > 6:
        print("\nInsira o código corretamente!\n")
    else:
        if voto == 1:
            cand1 += 1
        if voto == 2:
            cand2 += 1
        if voto == 3:
            cand3 += 1
        if voto == 4:
            cand4 += 1
        if voto == 5:
            nulo += 1
        if voto == 6:
            branco += 1

print("\nTotal de votos para cada candidato: ")
print("\nCandidato 1: ", cand1)
print("Candidato 2: ", cand2)
print("Candidato 3: ", cand3)
print("Candidato 4: ", cand4)
print("Total de votos nulos: ", nulo)
print("Total de votos em brancos: ", branco)