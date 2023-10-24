total = 0
juros = 0
while True:
    cod = int(input("Código do cliente (menor ou igual a 0 encerra): "))
    if cod <= 0:
        break
    print("\nTipo da conta\n")
    print("1. Poupança")
    print("2. Poupança Plus")
    print("3. Fundos de renda fixa\n")
    valor = float(input("Valor investido: "))
    total += valor
    opcao = int(input("Insira o que deseja fazer: "))
    match opcao:
        case 1:
            print("Rendimento mensal da poupança:",valor*1.015)
            juros += valor*1.015
        case 2:
            print("Rendimento mensal da poupança plus:",valor*1.02)
            juros += valor*1.02
        case 3:
            print("Rendimento mensal dos fundos de renda fixa:",valor*1.04)
            juros += valor*1.04
        case opcao if opcao >= 4 or opcao < 1:
            print("Opção inválida.")
    
print("Total investido:", total)
print("Total de juros pagos:", juros)