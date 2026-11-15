"""Conversor didático Celsius/Fahrenheit/Kelvin com zero absoluto validado."""
import math


def converter_temperaturas(unidade: int, temperatura: float) -> dict[str, float]:
    """Retorna as outras duas unidades, na mesma ordem da interface histórica."""
    if type(unidade) is not int or unidade not in (1, 2, 3):
        raise ValueError("Escolha 1 (Celsius), 2 (Fahrenheit) ou 3 (Kelvin).")
    if type(temperatura) not in (int, float) or not math.isfinite(temperatura):
        raise ValueError("Temperatura deve ser um número finito.")

    celsius = (
        temperatura if unidade == 1 else
        (temperatura - 32) * 5 / 9 if unidade == 2 else
        temperatura - 273.15
    )
    if celsius < -273.15 - 1e-9:
        raise ValueError("Temperatura abaixo do zero absoluto.")
    celsius = max(celsius, -273.15)
    fahrenheit = celsius * 1.8 + 32
    kelvin = celsius + 273.15
    if not all(math.isfinite(v) for v in (celsius, fahrenheit, kelvin)):
        raise ValueError("Conversão fora de intervalo numérico.")
    if unidade == 1:
        return {"Fahrenheit": fahrenheit, "Kelvin": kelvin}
    if unidade == 2:
        return {"Celsius": celsius, "Kelvin": kelvin}
    return {"Celsius": celsius, "Fahrenheit": fahrenheit}


def main() -> None:
    try:
        unidade = int(input("1 - Converter de Celsius\n2 - Converter de Fahrenheit\n3 - Converter de Kelvin\n"))
        temperatura = float(input("Digite a temperatura: "))
        resultados = converter_temperaturas(unidade, temperatura)
    except (ValueError, EOFError) as erro:
        raise SystemExit(f"Erro: {erro}")
    abreviacoes = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
    for nome, valor in resultados.items():
        print(f"Temperatura em {nome}: {valor:.2f} {abreviacoes[nome]}")


if __name__ == "__main__":
    main()
