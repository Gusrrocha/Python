while True:
    n1 = int(input("Insira o primeiro número: "))
    n2 = int(input("Insira o segundo número: "))
    while True:
        print("\nMenu de opções\n")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair\n")
        opcao = int(input("Insira o que deseja fazer: "))
        match opcao:
            case 1:
                print("\nAdição:",n1+n2,"\n")
            case 2:
                print("\nSubtração:",n1-n2,"\n")
            case 3:
                print("\nMultiplicação:",n1*n2,"\n")
            case 4:
                if n2 == 0:
                    print("\nNão se pode dividir por zero.","\n")
                else:
                    print("\nDivisão:",n1/n2,"\n")
            case 5:
                break
            case opcao if opcao >= 6 or opcao < 1:
                print("\n*Opção inválida.*")
