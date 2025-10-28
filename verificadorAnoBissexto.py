ano=int(input("Digite o ano: "))
if((ano % 100 != 0) and (ano % 4 == 0)) or (ano % 400 == 0):
    print(f"Ano {ano} é bissexto")
else:
    print(f"Ano {ano} não é bissexto")
