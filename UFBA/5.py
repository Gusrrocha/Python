t = int(input("Tamanho dos vetores: "))
vetor1 = []
vetor2 = []
vetor3 = []
for x in range(t):
    n1 = int(input("Número para o vetor nº 1: "))
    n2 = int(input("Número para o vetor nº 2: "))
    n3 = int(input("Número para o vetor nº 3: "))
    vetor1.append(n1)
    vetor2.append(n2)
    vetor3.append(n3)
norma1 = 0
norma2 = 0
norma3 = 0
soma1 = 0
soma2 = 0
soma3 = 0
maior = 0
for i in vetor1:
    soma1 += i
    norma1 += i
maior = norma1**1/2
for i in vetor2:
    soma2 += i
    norma2 += i
if norma2 > maior:
    maior = norma2**1/2
for i in vetor3:
    soma3 += i
    norma3 += i
if norma3 > maior:
    maior = norma3**1/2

print("Norma do vetor nº 1:", norma1**1/2)
print("Norma do vetor nº 2:", norma2**1/2)
print("Norma do vetor nº 3:", norma3**1/2)
print("Maior norma:", maior)
print("Vetor soma nº 1:", soma1)
print("Vetor soma nº 2:", soma2)
print("Vetor soma nº 3:", soma3)