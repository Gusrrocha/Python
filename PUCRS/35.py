maior = 0
menor = 0
alt = 0
alt_fem = 0
p_fem = 0
for i in range(50):
    altura = int(input("Insira a altura da pessoa (cm): "))
    sexo = int(input("Sexo da pessoa (1 para masculino; 2 para feminino): "))
    if i == 0:
        menor = altura
    elif altura < menor:
        menor = altura
    if altura > maior:
        maior = altura
    if sexo == 2:
        alt_fem += altura
        p_fem += 1
    alt += altura

print("Maior altura: ", maior)
print("Menor altura: ", menor)
print("Média altura das mulheres: ", alt_fem/p_fem)
print("Média altura das pessoas em geral: ", alt/50)
