#preço final, quantidade de parcelas e valor da parcela
valor = float(input("Insira o valor do carro: "))
compra = input("Parcelada ou à vista? (P ou V): ")
taxa = 1.03
if compra == 'V':
    valor *= 0.80
    parcelas = 1
elif compra == 'P':
    parcelas = int(input("Quantidade de parcelas (6,12,18,24,30,36,42,48,54,60): "))
    if parcelas % 6 == 0:
        for i in range(6,61):
            if i == parcelas:
                valor *= taxa
                break
            elif i % 6 == 0:
                taxa += 0.03
form = "{:.2f}".format(valor/parcelas)
form2 = "{:.2f}".format(valor)
print("\n{:<15} {:<15} {:<15}".format("Preço final", "Parcelas", "Valor da parcela"))
print("{:<15} {:<15} {:<15}".format("R$"+form2, str(parcelas)+"x", "R$"+form))


