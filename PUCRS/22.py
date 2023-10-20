habit = 0
maior_idade = 0
menor_idade = 0
contador = 0
salario = 0
sal_mul = 0
while True:
    idade = int(input("Insira a idade do indivíduo (negativo encerra o programa): "))
    if idade < 0:
        break
    if contador == 0:
        contador += 1
        menor_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if idade > maior_idade:
        maior_idade = idade
    sexo = input("Insira o sexo (M/F): ")
    sal_pes = float(input("Insir o salário: "))
    salario += sal_pes
    if sexo == 'F' and sal_pes <= 100:
        sal_mul += 1
    habit += 1

print("Média de salário do grupo: ", salario/habit)
print("Maior idade do grupo: ", maior_idade)
print("Menor idade do grupo: ", menor_idade)
print("Mulheres com salário de até R$ 100: ", sal_mul)