q_par = 0 
q_impar = 0
quant = 0
soma_par = 0
soma_geral = 0
while True:
    num = int(input("Insira um número positivo (0 encerra): "))
    if num == 0:
        break
    if num % 2 == 0:
        q_par += 1
        soma_par += num
    else:
        q_impar += 1
    quant += 1
    soma_geral += num
med_geral = soma_geral/quant
med_par = soma_par/q_par
print("Quantidade de valores pares: ", q_par)
print("Quantidade de valores impares: ", q_impar)
print("Média dos valores pares: ", med_par)
print("Média dos valores inseridos: ", med_geral)
