peso1 = 2
peso2 = 4
peso3 = 3
med_geral = 0
alunos = 0
for i in range(50):
    soma = 0
    for z in range(3):
        nota = float(input(f"\nInsira a nota nº{z+1}: "))
        match z:
            case 0:
                soma += nota*peso1
            case 1:
                soma += nota*peso2
            case 2:
                soma += nota*peso3
    med = soma/10
    med_geral += med
    print("\nMédia do aluno: ", med)
    if med >= 7:
        print("\nAprovado")
    elif med < 7:
        print("\nReprovado")
    alunos += 1
print("\nA média geral da turma é: ", med_geral/alunos)
                
