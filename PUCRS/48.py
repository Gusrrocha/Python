for i in range(75):
    cod_aluno = int(input("Insira código do aluno: "))
    nota = float(input("Insira a nota do aluno: "))
    match nota:
        case nota if nota < 5.0:
            print("Conceito D!")
        case nota if nota >= 5.0 and nota < 7.0:
            print("Conceito C!")
        case nota if nota >= 7.0 and nota < 9.0:
            print("Conceito B!")
        case nota if nota >= 9.0:
            print("Conceito A!")