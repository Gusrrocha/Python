while True:
    nota = 0
    cod_aluno = int(input("Insira o código do aluno (0 encerra o programa): "))
    if(cod_aluno == 0):
        print("Você saiu do programa!")
        break
    for i in range(3):
        nota += float(input("Insira a nota do aluno: "))
    media = nota/3
    print(f"Média do aluno de código '{cod_aluno}' é: {media}")