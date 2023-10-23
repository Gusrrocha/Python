valor_vista = 0
valor_parcelado = 0

for i in range(15):
    cod = input("Insira V para compras à vista ou P para parceladas: ")
    if cod != 'V' and cod != 'P':
        continue
    if cod != "":
        valor = float(input("Valor das compras: "))
        if cod == 'V':
            valor_vista += valor
        else:
            valor_parcelado += valor
            print("\nValor da primeira prestação: ", valor/3,"\n")
print("Total de compras à vista (valor): ", valor_vista)
print("Total de compras parceladas (valor): ", valor_parcelado)
print("O valor total das compras efetuadas: ", valor_parcelado+valor_vista)


        