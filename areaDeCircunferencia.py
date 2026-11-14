"""Área de círculo com quatro casas decimais (conforme o enunciado)."""
import math

PI = 3.14159265

def calcular_area(raio: float) -> float:
    if not isinstance(raio, (float, int)) or not math.isfinite(raio) or raio < 0:
        raise ValueError("O raio deve ser um número finito e não negativo.")
    return PI * (raio ** 2)

def main() -> None:
    try:
        raio = float(input("Digite o valor do raio, utilize o . para ponto flutuante: "))
        print(f"A={calcular_area(raio):.4f}")
    except ValueError as erro:
        raise SystemExit(f"Erro: {erro}")

if __name__ == "__main__":
    main()
