maior = 0
maior_cid = 0
menor = 0
menor_cid = 0
med_vei = 0
med_aci = 0
cidade = 0
for i in range(200):
    cod_cidade = int(input("Código da cidade: "))
    estado = input("Estado (sigla): " )
    num_v_pas = int(input("Número de veículos de passeio: "))
    num_a_t_c_v = int(input("Número de acidentes de trânsito com vítimas (em 1992): "))
    if i == 0:
        menor = num_a_t_c_v
        menor_cid = cod_cidade
    elif num_a_t_c_v < menor:
        menor = num_a_t_c_v
        menor_cid = cod_cidade
    if num_a_t_c_v > maior:
        maior = num_a_t_c_v
        maior_cid = cod_cidade
    med_vei += num_v_pas
    if estado == 'RS':
        med_aci += num_a_t_c_v
    cidade += 1
    
print(f"\nO maior índice de acidentes é na cidade com código {maior_cid}.")
print(f"\nO menor índice de acidentes é na cidade com código {menor_cid}.")
print(f"\nA média de veículos nas cidades brasileiras é: {med_vei/cidade}.")    
print(f"\nA média de acidentes com vítimas nas cidades do Rio Grande do Sul é: {med_aci/cidade}.")