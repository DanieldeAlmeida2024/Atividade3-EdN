peso=float(input("Digite o seu peso em Kg: "))
altura=float(input("Digite a sua altura em metros: "))
IMC = peso / (altura ** 2)
print(f"Seu IMC: {IMC}")
if(IMC < 18.5):
    print(f"Abaixo do peso")
elif(IMC < 25):
    print(f"Peso normal")
elif(IMC < 30):
    print(f"Sobrepeso")
else:
    print(f"Obeso")