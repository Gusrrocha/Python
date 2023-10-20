while True:
    cod_prod = int(input("Entre com o código do produto (negativo encerra): "))
    if cod_prod < 0:
        print("\nVocê saiu do programa!")
        break
    preco = float(input("Digite o custo do produto: "))
    preco_novo = preco*1.20
    med_preco = (preco+preco_novo)/2
    print("\nCódigo do Produto: ", cod_prod)
    print("O preço do produto após o aumento é: ", preco_novo)
    print("A média entre o preço antigo e o novo é: ", med_preco)
