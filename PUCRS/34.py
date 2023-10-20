cod_alto = 0
cod_baixo = 0
alto = 0
baixo = 0
for i in range(5):
    cod_aluno = int(input("Código do aluno: "))
    altura = int(input("Altura do aluno (cm): "))
    if i == 0:
        baixo = altura
    elif altura < baixo:
        baixo = altura
        cod_baixo = cod_aluno
    if altura > alto:
        alto = altura
        cod_alto = cod_aluno
print(f"Aluno de código {cod_alto} é o mais alto, com uma altura de: {alto}")
print(f"Aluno de código {cod_baixo} é o mais baixo, com uma altura de: {baixo}")