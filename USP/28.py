quant_filho = 0
salario = 0
salario_total = 0
maior_sal = 0
pessoas_150minus = 0
habit = 0
lista_sal = []
med_sal = 0
percent_sal = 0
while True:
    salario = float(input("Insira o valor do salário da pessoa: "))
    if salario < 0:
        break
    if salario > maior_sal:
        maior_sal = salario
    if salario <= 150:
        pessoas_150minus += 1
    salario_total += salario
    habit += 1
    quant_filho += int(input("Insira a quantidade de filhos que essa pessoa tem: "))
    lista_sal.append(salario)

if(habit > 0):
    print(" ")
    print("----------- DADOS ------------")
    print(" ")
    med_sal = salario_total/habit
    percent_sal = pessoas_150minus/habit
    print("Média do salário da população: ", med_sal)
    print("Média do número de filhos: ", quant_filho/habit)
    print("Maior Salário: ", maior_sal)
    print("Percentual de pessoas com até R$ 150.00: ", float(percent_sal*100)," %")

                    