preco = 5.00
ingressos = 120
while preco >= 1.00:
    print(f"Lucro esperado com o valor de R$ {preco:.2f}: R$", preco*ingressos)
    print("A quantidade de ingressos vendidos foi: ", ingressos)
    ingressos += 26
    preco -= 0.50
    