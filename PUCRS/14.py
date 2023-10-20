q_num = 0
q_pos = 0
q_neg = 0
soma = 0
while True:
    num = input("Insira um número (se não inserir número, encerra o programa): ")
    try:
        num = float(num)
        if num < 0:
            q_neg += 1
        if num >= 0:
            q_pos += 1
        q_num += 1
        soma += num
    except:
        break
print("Média dos valores lidos: ", soma/q_num)
print("Quantidade de valores positivos lidos: ", q_pos)
print("Quantidade de valores negativos lidos: ", q_neg)
print("Percentual de valores positivos: ", (q_pos/q_num)*100)
print("Percentual de valores negativos: ", (q_neg/q_num)*100)
