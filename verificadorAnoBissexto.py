"""Verifica anos bissextos no calendário gregoriano."""
def eh_bissexto(ano: int) -> bool:
    if type(ano) is not int or ano < 1:
        raise ValueError("Informe um ano inteiro positivo.")
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

def main() -> None:
    try:
        ano = int(input("Digite o ano: "))
        if eh_bissexto(ano):
            print(f"Ano {ano} é bissexto")
        else:
            print(f"Ano {ano} não é bissexto")
    except ValueError as erro:
        raise SystemExit(f"Erro: {erro}")

if __name__ == "__main__":
    main()
