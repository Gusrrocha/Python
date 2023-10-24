while True:
    print("\nMenu de opções\n")
    print("1. Média aritmética")
    print("2. Média ponderada")
    print("3. Sair\n")
    opcao = int(input("Insira o que deseja fazer: "))
    match opcao:
        case 1:
            nota1 = int(input("Insira a primeira nota: "))
            nota2 = int(input("Insira a segunda nota: "))
            print("Média aritmética:",(nota1+nota2)/2)
        case 2:
            nota1 = int(input("Insira a primeira nota: "))
            peso1 = int(input("Insira o peso: "))
            nota2 = int(input("Insira a segunda nota: "))
            peso2 = int(input("Insira o peso: "))
            nota3 = int(input("Insira a terceira nota: "))
            peso3 = int(input("Insira o peso: "))
            soma = (nota1*peso1)+(nota2*peso2)+(nota3*peso3)
            print("\n-> Média ponderada:", soma/(peso1+peso2+peso3))
        case 3:
            break
        case opcao if opcao >= 4 or opcao < 1:
            print("Opção inválida.")