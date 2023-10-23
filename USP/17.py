idade_ac = 0
mul = 0
hom = 0
mul_idade = 0
hom_idade = 0
for x in range(7):
    idade = int(input("Insira a idade: "))
    sexo = input("F para feminino e M para masculino: ")
    idade_ac += idade
    if sexo == 'F':
        mul += 1
        mul_idade += idade
    if sexo == 'M':
        hom += 1
        hom_idade += idade

print("Idade média: ", idade_ac/7)
print("Idade média (F): ", mul_idade/mul)
print("Idade média (M): ", hom_idade/hom)