lista = []
while True:
    lista_temp = []
    nome = input("Nome completo do cliente: ")
    rg = int(input("RG do cliente (apenas números): "))
    cpf = int(input("CPF do cliente (apenas números): "))
    tel = int(input("Telefone do cliente (apenas números): "))
    lista_temp.append(nome)
    lista_temp.append(rg)
    lista_temp.append(cpf)
    lista_temp.append(tel)
    lista.append(lista_temp)
    sair = input("Continuar? (s/n): ")
    if sair == 'n':
        break

print("{:<20} {:<20} {:<20} {:<20}".format("Nome", "RG", "CPF", "Telefone"))
for cliente in lista:    
    print("{:<20} {:<20} {:<20} {:<20}".format(cliente[0],cliente[1],cliente[2],cliente[3]))
