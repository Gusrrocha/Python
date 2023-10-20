n = int(input("Tamanho do conjunto: "))
subel = int(input("Insira o número de elementos que você queira separar: "))
fat = n
pfat = subel
diffat = n-subel
for i in range(1, n):
    fat *= i
for i in range(1, subel):
    pfat *= i
for i in range(1, n-subel):
    diffat *= i
arranjo = fat/diffat
combinacao = fat/(pfat*diffat)
print("Arranjo: ", arranjo)
print("Combinação: ", combinacao)