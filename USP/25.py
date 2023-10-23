maior = 0
menor = 0
c = 0
reprovado = 0
fre_reprov = 0
for i in range(10):
    soma = 0
    cod_aluno = int(input("Insira o código de matrícula do aluno: "))
    frequencia = int(input("Número de aulas frequentadas: "))
    for i in range(3):
        nota = float(input(f"Insira a {i+1}º nota do aluno: "))
        if c == 0:
            menor = nota
            c += 1
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        soma += nota
    media = soma/3
    print("Calculando...")
    print("\n-------- Dados --------\n")
    print("Matrícula do aluno: ", cod_aluno)
    print("A média das notas é: ", media)
    if media >= 6 and frequencia >= 40:
        print("APROVADO")
    elif media < 6:
        print("REPROVADO")
        reprovado += 1
    elif frequencia < 40:
        print("REPROVADO POR FALTA")
        fre_reprov += 1
print("A maior nota da turma é: ", maior)
print("A menor nota da turma é: ", menor)
print("O total de alunos reprovados: ", reprovado)
print("Porcentagem de alunos reprovados por frequência: ", (fre_reprov/10)*100,"%")
