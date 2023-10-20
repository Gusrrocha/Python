
peso1 = 4
peso2 = 3
while True:
    lista_notas = []
    maior = 0
    soma = 0
    contador = 1
    cnt = 0
    cod_aluno = int(input("Insira o código do aluno (0 para encerrar o programa): "))
    if cod_aluno < 0:
        print("Você saiu do programa!")
        break
    for i in range(3):
        nota = float(input("Insira a nota do aluno: "))
        lista_notas.append(nota)
        if nota > maior:
            maior = nota
    print("Calculando...")
    print("\n-------- Dados --------\n")
    print("Código do aluno: ", cod_aluno)
    for item in lista_notas:
        print(f"Nota {contador}: ", item)
        if item == maior and cnt == 0:
            cnt += 1
            soma += item*peso1
        elif cnt > 0 or item != maior:
            soma += item*peso2
        contador += 1
    media = float(soma/(peso1+peso2*2))
    print("A média das notas é (Considerando seus pesos): ", media)
    if media >= 5:
        print("APROVADO")
    elif media < 5:
        print("REPROVADO")