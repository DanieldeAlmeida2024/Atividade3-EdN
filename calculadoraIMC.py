"""Cálculo didático de IMC com validação de peso e altura."""
import math

def calcular_imc(peso: float, altura: float) -> float:
    if not all(isinstance(valor, (int, float)) and math.isfinite(valor) and valor > 0
               for valor in (peso, altura)):
        raise ValueError("Peso e altura devem ser números finitos maiores que zero.")
    return peso / altura ** 2

def classificar_imc(imc: float) -> str:
    if not isinstance(imc, (float, int)) or not math.isfinite(imc) or imc <= 0:
        raise ValueError("IMC deve ser um número finito positivo.")
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obeso"

def main() -> None:
    try:
        peso = float(input("Digite o seu peso em Kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC: {imc:.2f}")
        print(classificar_imc(imc))
    except ValueError as erro:
        raise SystemExit(f"Erro: {erro}")

if __name__ == "__main__":
    main()
