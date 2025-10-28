unidadeMedida=int(input("1 - Converter de Celsius\n2 - Converter de Fahrenheit\n3 - Converter de Kelvin\n"))
temperatura=float(input("Digite a temperatura: "))
if(unidadeMedida == 1):
    print(f"Temperatura em Fahrenheit: {(temperatura*1.8)+32:.2f} F")
    print(f"Temperatura em Kelvin: {temperatura+273.15:.2f} K")
elif(unidadeMedida == 2):
    print(f"Temperatura em Celsius: {(temperatura-32)*(5/9):.2f} C")
    print(f"Temperatura em Kelvin: {(temperatura-32) * (5/9) + 273.15 :.2f} K")
elif(unidadeMedida == 3):
    print(f"Temperatura em Celsius: {temperatura-273.15:.2f} C")
    print(f"Temperatura em Fahrenheit: {(temperatura-273.15) * 1.8 + 32 :.2f} F")