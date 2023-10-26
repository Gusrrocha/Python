gabarito = []
alunos = []
for x in range(20):
    resposta = int(input(f"Resposta da {x+1}º questão: "))
    gabarito.append(resposta)
for i in range(2):
    aluno = []
    acertos = 0
    nome = input("Insira o nome do aluno: ")
    for x in range(20):
        resposta = int(input(f"Resposta da {x+1}º questão para o aluno {x+1}: "))
        if resposta == gabarito[x]:
            acertos += 1
    nota = acertos*0.5
    aluno.append(nome)
    aluno.append(nota)
    alunos.append(aluno)
for item in alunos:
    print(f"\nNome:", item[0])
    if item[1] >= 6:
        print("Aprovado")
    else:
        print("Reprovado")