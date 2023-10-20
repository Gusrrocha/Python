fora = 0
dentro = 0
for i in range(10):
    num = int(input("Insira um número: "))
    if num in range(10,21):
        dentro += 1
    if num not in range(10,21):
        fora += 1
print("Dentro do intervalo [10,20]: ", dentro)
print("Fora do intervalo [10,20]: ", fora)
