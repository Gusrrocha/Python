q_4, q_5, q_7, q_12, total = 0,0,0,0,0
while True:
    num = int(input("Número do canal [4,5,7,12](0 encerra): "))
    if num == 0:
        break
    pessoas = int(input("Número de pessoas assistindo esse canal: "))
    if num == 4:
        q_4 += pessoas
    if num == 5:
        q_5 += pessoas
    if num == 7:
        q_7 += pessoas
    if num == 12:
        q_12 += pessoas
    total += pessoas
print("Porcentagem de audiência canal 4: ", (q_4/total)*100, '%')
print("Porcentagem de audiência canal 5: ", (q_5/total)*100, '%')
print("Porcentagem de audiência canal 7: ", (q_7/total)*100, '%')
print("Porcentagem de audiência canal 12: ", (q_12/total)*100, '%')