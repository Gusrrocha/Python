while True:
    print("\nMenu de opções\n")
    print("1. Novo salário")
    print("2. Férias")
    print("3. Décimo terceiro")
    print("4. Sair\n")
    opcao = int(input("Insira o que deseja fazer: "))
    match opcao:
        case 1:
            salario = float(input("Digite o salário: "))
            if salario < 350:
                print("O novo salário do funcionário é:", salario*1.15)
            if salario in range(350,601):
                print("O novo salário do funcionário é:", salario*1.10)
            if salario > 600:
                print("O novo salário do funcionário é:", salario*1.05)
        case 2:
            salario = float(input("Digite o salário: "))
            ferias = salario+1/3
            print("As férias do funcionário é:", ferias)
        case 3:
            salario = float(input("Digite o salário: "))
            while True:
                meses = int(input("Digite o número de meses trabalhados (max. 12): "))
                if meses > 12 or meses < 0:
                    if meses > 12:
                        print("O máximo de meses é 12.")
                    elif meses < 0:
                        print("Não existe meses negativos...")
                else:
                    break
            dec = salario*meses/12
            print("Décimo terceiro:", dec)
        case 4:
            break
        case opcao if opcao >= 5 or opcao < 1:
            print("\n*Opção inválida.*")