while True:
    soma = 0
    it1 = []
    it2 = []
    it3 = []
    n1 = int(input("Insira o primeiro extremo do intervalo: "))
    n2 = int(input("Insira o segundo extremo do intervalo: "))
    if n1 == n2:
        print("\n*NÃO INSIRA DOIS EXTREMOS IGUAIS*\n")
        pass
    else:
        for x in range(n1, n2+1):
            soma += 1
        if int(soma % 3) == 0:
            for x in range(n1, int((soma/3))+1):
                it1.append(x)
            for x in range(len(it1)+1, int(((soma/3))*2)+1):
                it2.append(x)
            for x in range(len(it2)+len(it1)+1, (soma)+1):
                it3.append(x)
            print(it1)
            print(it2)
            print(it3)        
        else:
            print("\n*Insira um intervalo que seja divisível por 3.*\n")