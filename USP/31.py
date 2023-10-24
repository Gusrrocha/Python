luc_sup, luc_inf, lucro_total = 0,0,0
while True:
    tipo = input("Tipo da ação (letra)(F encerra): ")
    if tipo == 'F':
        break
    preco = float(input("Insira o preço de compra: "))
    venda = float(input("Insira o preço de venda: "))
    lucro = venda-preco
    print(f"Lucro da ação {tipo}: {lucro}")
    if lucro > 1000:
        luc_sup += 1
    if lucro < 200:
        luc_inf += 1
    lucro_total += lucro

print(f"Quantidade de ações com lucro superior a R$ 1.000,00: {luc_sup}")
print(f"Quantidade de ações com lucro inferior a R$ 200,00: {luc_inf}")
print(f"Lucro total da empresa: {lucro_total}")

