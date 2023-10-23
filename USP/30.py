soma_novo = 0
soma_velho = 0
produto = 0
while True:
    cod_prod = int(input("Entre com o código do produto (negativo encerra): "))
    if cod_prod < 0:
        print("\nVocê saiu do programa!")
        break
    preco = float(input("Digite o custo do produto: "))
    preco_novo = preco*1.20
    soma_novo += preco_novo
    soma_velho += preco
    produto += 1
    print("\nCódigo do Produto: ", cod_prod)
    print("O preço do produto após o aumento é: ", preco_novo)

print("A média dos preços velhos: ", soma_velho/produto)
print("A média dos preços novos: ", soma_novo/produto)


