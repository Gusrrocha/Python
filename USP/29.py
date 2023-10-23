habit = 0
maior_idade = 0
menor_idade = 0
contador = 0
salario = 0
sal_mul = 0
s_menor = 0
sexo_menor = ''
idade_menor = 0
while True:
    idade = int(input("Insira a idade do indivíduo (negativo encerra o programa): "))
    if idade < 0:
        break
    sexo = input("Insira o sexo (M/F): ")
    sal_pes = float(input("Insira o salário: "))
    if contador == 0:
        contador += 1
        s_menor = sal_pes
        idade_menor = idade
        if sexo == 'F':
            sexo_menor = 'F'
        elif sexo == 'M':
            sexo_menor = 'M'   
        menor_idade = idade
    if sal_pes < s_menor:
        s_menor = sal_pes
        if sexo == 'F':
            sexo_menor = 'F'
        elif sexo == 'M':
            sexo_menor = 'M' 
        idade_menor = idade
    if idade < menor_idade:
        menor_idade = idade
    if idade > maior_idade:
        maior_idade = idade   
    salario += sal_pes
    if sexo == 'F' and sal_pes <= 200:
        sal_mul += 1

    habit += 1

print("Média de salário do grupo: ", salario/habit)
print("Maior idade do grupo: ", maior_idade)
print("Menor idade do grupo: ", menor_idade)
print("Mulheres com salário de até R$ 200: ", sal_mul)
print("Idade da pessoa com menor salário:", idade_menor,
      "\nSexo:",sexo_menor)