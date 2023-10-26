gabarito = []
for x in range(20):
    resposta = int(input(f"Resposta da {x+1}º questão: "))
    gabarito.append(resposta)
for i in range(50):
    acertos = 0
    nome = input("Insira o nome do aluno: ")
    for x in range(20):
        resposta = int(input(f"Resposta da {x+1}º questão para o aluno {x+1}: "))
        if resposta == gabarito[x]:
            acertos += 1
    print(f"O aluno acertou {acertos} questões!")
    nota = acertos*0.5
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")