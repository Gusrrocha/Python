negativo = 0
for i in range(5):
    a = int(input("Insira um valor positivo ou negativo: "))
    if a < 0:
        negativo += 1
if negativo == 0:
    print("Todos os dados informados são positivos!")
if negativo == 1:
    print("Dos dados informados apenas 1 (um) é negativo")
if negativo > 1:
    print(f"Dos dados informados {negativo} são negativos!")