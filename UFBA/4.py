l_idade = []
l_nome = []
l_valor = []
valor = float(input("Valor base de indenização por um plano de saúde: "))
cont = 0
while True:
    idade = int(input("Idade do paciente indenizado: "))
    nome = input("Nome completo do paciente indenizado: ")
    valor_i = valor
    l_idade.append(idade)
    l_nome.append(nome)
    if idade <= 12:
        valor_i *= 1.3
    elif idade >= 13 and idade <= 49:
        valor_i *= 1.1
    elif idade >= 50 and idade <= 65:
        valor_i *= 1.15
    elif idade > 65:
        valor_i *= 1.35
    cont += 1
    l_valor.append(valor_i)
    sair = input("\nDeseja sair do programa e calcular os resultados? (S, N): ")
    if sair == 'S':
        break
    elif sair == "N":
        continue
ind = 0
print("\n{:<15} {:<15} {:<15} {:<15}".format("Cliente", "Idade", "Valor (base)", "Valor (Reajustado)"))
for item in range(1, cont+1):
    print("{:<15} {:<15} {:<15} {:<15}".format(l_nome[ind], l_idade[ind], valor, l_valor[ind]))
    if item % 3 == 0:
        ind = 0
    ind += 1

