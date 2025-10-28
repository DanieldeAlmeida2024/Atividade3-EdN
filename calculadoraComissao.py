nome = input("Digite o nome: ")
salarioFixo = float(input("Digite o salário fixo: "))
totalVendas = float(input("Digite o total de vendas: "))
taxaComissao = 0.15 
comissao = totalVendas * taxaComissao

print(f"TOTAL = R$ {salarioFixo + comissao:.2f}")