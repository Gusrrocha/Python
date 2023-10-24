inf35, positivo, p_50100, p_1020, numeros, p_50minus = 0,0,0,0,0,0
while True:
    num = float(input("Insira um número: "))
    if num < 35:
        inf35 += 1
    if num > 0:
        positivo += num
    if num >= 50 and num <= 100:
        p_50100 += 1
    if num >= 10 and num <= 20:
        p_1020 += 1
    if num < 50:
        p_50minus += 1
    numeros += 1
    sair = input("Deseja sair e calcular? (S/N): ")
    if sair == 'S':
        break
print(f"Quantidade de número menores que 35: {inf35}")
print(f"Média dos números positivos: {positivo/numeros}")
print(f"Porcentagem de números entre 50 e 100: {(p_50100/numeros)*100}")
if p_50minus != 0:
    print(f"Porcentagem de números entre 10 e 20 menores que 50: {(p_1020/p_50minus)*100}")

