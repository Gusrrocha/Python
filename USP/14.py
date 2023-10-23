verde = 0
azul = 0
ol_castanho = 0
ol_preto = 0
louro = 0
ca_castanho = 0
preto = 0
ruivo = 0
pessoas = 0
q_idpe = 0
p_alt = 0
raz = 0
for i in range(20):
    idade = int(input("Insira a idade: "))
    cor_olho = input("Insira a cor do olho (A para azul, V para verde, C para castanho e P para preto): ")
    peso = float(input("O peso da pessoa em kg: "))
    altura = int(input("A altura da pessoa em cm: "))
    
    if idade > 50 and peso < 60:
        q_idpe += 1
    if altura < 150:
        p_alt += 1
    if cor_olho == 'A':
        azul += 1
    elif cor_olho == 'V':
        verde += 1
    elif cor_olho == 'C':
        ol_castanho += 1
    elif cor_olho == 'P':
        ol_preto += 1


    cor_cabelo = input("Insira a cor do cabelo (L para louro, P para preto, C para castanho e R para ruivo): ") 
    if cor_cabelo == 'L':
        louro += 1
    elif cor_cabelo == 'C':
        ca_castanho += 1
    elif cor_cabelo == 'P':
        preto += 1
    elif cor_cabelo == 'R':
        ruivo += 1
        if cor_olho != 'A':
            raz += 1
    pessoas += 1

print("Quantidade de pessoas com mais de 50 anos e menos de 60 kg: ", q_idpe)
print("Média da idade das pessoas com menos de 150 cm de altura: ", p_alt/pessoas)
print("Porcentagem pessoas com olhos azuis: ", (azul/pessoas)*100,"%")
print("Quantidade de pessoas ruivas sem olhos azuis: ", raz)
