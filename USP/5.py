for cliente in range(15):
    nome = input("Digite o nome do cliente: ")
    valor_p = float(input("Digite o valor da compra do ano passado: "))
    if (valor_p < 1000.00):
        print(f"O cliente {nome} tem um bônus de 10% no valor de: ", valor_p*0.10)
    else:
        print(f"O cliente {nome} tem um bônus de 15% no valor de: ", valor_p*0.15)
