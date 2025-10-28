idade=int(input("Digite sua idade: "))

if(idade <= 12):
    print(f"Criança")
elif(idade <= 17):
    print(f"Adolescente")
elif(idade <= 59):
    print(f"Adulto")
else:
    print(f"Idoso")
    