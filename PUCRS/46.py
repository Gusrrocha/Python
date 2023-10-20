verde = 0
azul = 0
ol_castanho = 0
louro = 0
ca_castanho = 0
preto = 0
maior_idade = 0
habit = 0
quant_fem = 0
while True:
    idade = int(input("Insira a idade (negativo encerra): "))
    if idade < 0:
        break
    if idade > maior_idade:
        maior_idade = idade
    sexo = input("Insira o sexo (M/F): ")
    cor_olho = input("Insira a cor do olho (A para azul, V para verde e C para castanho): ")
    if cor_olho == 'A':
        azul += 1
    elif cor_olho == 'V':
        verde += 1
    elif cor_olho == 'C':
        ol_castanho += 1
    cor_cabelo = input("Insira a cor do cabelo (L para louro, P para preto e C para castanho): ") 
    if cor_cabelo == 'L':
        louro += 1
    elif cor_cabelo == 'C':
        ca_castanho += 1
    elif cor_cabelo == 'P':
        preto += 1
    if sexo == 'F' and cor_olho == 'V' and cor_cabelo == 'L' and idade >= 18 and idade <= 35:
        quant_fem += 1
    habit += 1
print("A maior idade entre os habitantes é: ", maior_idade)
print("A quantidade de mulheres cuja idade esteja entre 18 e 35 anos, que tenha olhos verdes e cabelos louros é: ", quant_fem)